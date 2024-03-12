from flask import Flask, Response, render_template, send_from_directory, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
from style import blog
from readMarkdown import extract_markdown
import psycopg2


# global variables
DEFAULT = None
basedir = os.path.abspath(os.path.dirname(__file__))

# flask variables
app = Flask(__name__)

DEBUG = False
RESET = False
PRODUCTION_VERSION = True
TESTING = False
if PRODUCTION_VERSION:
    if TESTING:
        from dotenv import load_dotenv
        # Load environment variables from .env file
        load_dotenv()
    # Access the environment variables
    hostname = os.getenv("db_hostname")
    port = int(os.getenv("db_port"))
    database = os.getenv("db_database")
    username = os.getenv("db_username")
    password = os.getenv("db_password")
    
    class DBSession:
        def __init__(self, conn): self.conn = conn
        def add(self, p): p.add()
        def commit(self): self.conn.commit()
        def delete(self, p): p.delete()
            

    class DB:
        def __init__(self, hostname, port, database, username, password):
            # Construct the connection string
            connection_string = f"dbname={database} user={username} password={password} host={hostname} port={port}"
            self.conn = psycopg2.connect(connection_string)
            self.session = DBSession(self.conn)
            
    db = DB(hostname=hostname, port=port, database=database, username=username, password=password)
        
    # class goodDict:
    #     def __init__(self, data:dict):
    #         self.data = data
    #     def __getattr__(self, item):
    #         return self.data.get(item)

        
    class USER:
        class query: 
            def all():
                cur = db.conn.cursor()
                cur.execute(f"SELECT * FROM users")
                rows = cur.fetchall()
                cur.close()
                return [USER(**{
                    'id':row[0],
                    'userName':row[1],
                    'userDescription':row[2],
                    'userPNG':row[3],
                    'userFollowers':row[4]
                }) for row in rows]
            def get(id):
                cur = db.conn.cursor()
                cur.execute(f"SELECT * FROM users WHERE id = {id}")
                row = cur.fetchone()
                cur.close()
                return USER(**{
                    'id':row[0],
                    'userName':row[1],
                    'userDescription':row[2],
                    'userPNG':row[3],
                    'userFollowers':row[4]
                })
        def __init__(self, userName, userDescription, userPNG, userFollowers, id=None):
            self.userName = userName
            self.userDescription = userDescription
            self.userPNG = userPNG
            self.userFollowers = userFollowers
            self.id = id
        # userFollowers_id = 
        # repr method represents how one object of this datatable will look like
        def __repr__(self):
            return f"Name : {self.userName}, userDescription: {self.userDescription}, userPNG: {self.userPNG}, userFollowers: {self.userFollowers}"

        def add(self):
            cur = db.conn.cursor()
            cur.execute('INSERT INTO users (userName, userDescription, userPNG, userFollowers)'
                        'VALUES (%s, %s, %s, %s)',
                        (self.userName,
                         self.userDescription,
                         self.userPNG,
                         self.userFollowers)
                        )
            cur.close()
        def delete(self):
            if self.id is not None:
                cur = db.conn.cursor()
                cur.execute(f"DELETE FROM users WHERE id = {self.id}")
                cur.close()
        
            
    class BLOG:
        class query: 
            def all():
                cur = db.conn.cursor()
                cur.execute(f"SELECT * FROM blogs")
                rows = cur.fetchall()
                cur.close()
                return [BLOG(**{
                    'id':row[0],
                    'user_id':row[1],
                    'title':row[2],
                    'desc':row[3],
                    'data':row[4]
                }) for row in rows]
            def get(id):
                cur = db.conn.cursor()
                cur.execute(f"SELECT * FROM blogs WHERE id = {id}")
                row = cur.fetchone()
                cur.close()
                return BLOG(**{
                    'id':row[0],
                    'user_id':row[1],
                    'title':row[2],
                    'desc':row[3],
                    'data':row[4]
                })
        def __init__(self, user_id, title, desc, data, id=None):
            self.user_id = user_id
            self.title = title
            self.desc = desc
            self.data = data
            self.id=id

        # repr method represents how one object of this datatable will look like
        def __repr__(self):
            return f"{self.id}). Name : {self.user_id}, title: {self.title}, desc: {self.desc}, data: {self.data}"

        def add(self):
            cur = db.conn.cursor()
            cur.execute('INSERT INTO blogs (user_id, title, description, data)'
                        'VALUES (%s, %s, %s, %s)',
                        (self.user_id,
                         self.title,
                         self.desc,
                         self.data)
                        )
            cur.close()
            
        def delete(self):
            if self.id is not None:
                cur = db.conn.cursor()
                cur.execute(f"DELETE FROM blogs WHERE id = {self.id}")
                cur.close()
    print("initializing production database ...")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database\\database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app) # Creating an SQLAlchemy instance

    class BLOG(db.Model):
        # Id : Field which stores unique id for every row in 
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, unique=False, nullable=False)
        title = db.Column(db.String(100), unique=False, nullable=False)
        desc = db.Column(db.String(200), unique=False, nullable=True)
        data = db.Column(db.String(5000), unique=False, nullable=False)
        # date_added
    
        # repr method represents how one object of this datatable will look like
        def __repr__(self):
            return f"{self.id}). Name : {self.user_id}, title: {self.title}, desc: {self.desc}, data: {self.data}"

    class USER(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        userName = db.Column(db.String(20), unique=False, nullable=False)
        userDescription = db.Column(db.String(300), unique=False, nullable=False)
        userPNG = db.Column(db.String(50), unique=False, nullable=False)
        userFollowers = db.Column(db.Integer, unique=False, nullable=False)
        # userFollowers_id = 
        # repr method represents how one object of this datatable will look like
        def __repr__(self):
            return f"{self.id}). Name : {self.userName}, userDescription: {self.userDescription}, userPNG: {self.userPNG}, userFollowers: {self.userFollowers}"

# function to add profiles
@app.route('/api/createUser', methods=["POST"])
def createUser():
    userName = request.form.get("user_name")
    userDescription = request.form.get("userDescription")
    userPNG = request.form.get("userPNG")
    userFollowers = 0

    # create an object of the Profile class of models
    # and store data as a row in our datatable
    if userName != '' and userDescription != '' and userPNG != '':
        p = USER(userName=userName, userDescription=userDescription, userPNG=userPNG, userFollowers=userFollowers)
        db.session.add(p)
        db.session.commit()
        return jsonify({
            'OK':True
        })
    else:
        return jsonify({
            'OK':False
        })
@app.route('/api/deleteUser', methods=["POST"])
def deleteUser():
    #TODO delete all blog posts from the database
    id = request.form.get("id")
    user = USER.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({
            'OK':True
        })
    else:
        return jsonify({
            'OK':False
        })
@app.route('/api/listUser')
def allUsers():
    return jsonify({
            'users':[{
                        'id': i.id,
                        'userName' : i.userName,
                        'userDescription' : i.userDescription,
                        'userPNG' : i.userPNG,
                        'userFollowers': i.userFollowers
                    } for i in USER.query.all()]
    })

@app.route('/api/post', methods=["POST"])
def post():
    user_id = request.form.get("user_id")
    title = request.form.get("title")
    data = request.form.get("data")
    desc = request.form.get("desc", default=None)

    # create an object of the Profile class of models
    # and store data as a row in our datatable
    if user_id != None and title != '' and data != '':
        p = BLOG(user_id=user_id, title=title, data=data, desc=desc)
        db.session.add(p)
        db.session.commit()
        return jsonify({
            'OK':True
        })
    else:
        return jsonify({
            'OK':False
        })     
@app.route('/api/delete', methods=["POST"])
def erase():
    id = request.form.get("id")
    # Deletes the data on the basis of unique id
    data = BLOG.query.get(id)
    if data:
        db.session.delete(data)
        db.session.commit()
        return jsonify({
            'OK':True
        })
    else:
        return jsonify({
            'OK':False
        })
@app.route('/api/list')
def sendAll():
    return jsonify({
            'blogs':[{
                        'id': i.id,
                        'user_id' : i.user_id,
                        'title' : i.title,
                        'desc' : i.desc,
                        'data' : i.data
                    } for i in BLOG.query.all()]
    })

@app.route('/<int:id>')
def blogPage(id):
    data = BLOG.query.get(id)
    print(data)
    print(data.user_id)
    user = USER.query.get(data.user_id)
    if data:
        b = blog(user=user.userName,
            userPNG=user.userPNG,
            userFollowers=user.userFollowers,
            userDescription=user.userDescription,
            title=data.title,
            subtitle=data.desc,
            post_date='Sep 28',
            read_time='18 min',
            reactions={
                'claps': '51',
                'Responds': '1'
            },
            tags=['Machine Learning', 'Deep Learning', 'Data Science', 'Artificial Intelligence', 'Python'])    
        b.add(extract_markdown(data.data))
        return render_template('blog.html', 
                               title=b.title,
                               headingHTML = b.getHeadingHTML(),
                               contentHTML = b.html, 
                               rootFooterHTML = b.getRootFooterHTML(),
                               data=b.html)
    else:  return "404 not found"

@app.route('/')
def home():
    return render_template('home.html', data='<div>'+''.join([f'<div><a href="/{i.id}">{i.title}</a></div>' for i in BLOG.query.all()])+'</div>')

def resetDatabase():
    print("Database reset...")
    os.remove(os.path.join('database', os.listdir('database')[0]))
if not os.path.exists(os.path.join(basedir, 'database\\database.db')):
    print('creating database ...')
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    if RESET: resetDatabase()
    app.run(debug=DEBUG, host='0.0.0.0', port=5000)
