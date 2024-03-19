from flask import Flask, Response, render_template, send_from_directory, jsonify, request, redirect, url_for
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os, re, random
from style import blog
from readMarkdown import  extract_markdown
# global variables
DEFAULT = None
basedir = os.path.abspath(os.path.dirname(__file__))

# flask variables
app = Flask(__name__)
app.config["SECRET_KEY"] = "abc"

DEBUG = False
RESET = False
PRODUCTION_VERSION = True
TESTING = False
if PRODUCTION_VERSION:
    from flask_postgresql import PostgreSQL
    # from flask_postgresql_test import PostgreSQL
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
    db = PostgreSQL(hostname=hostname, port=port, database=database, username=username, password=password)
else:
    from flask_sqlalchemy import SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database\\database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app) # Creating an SQLAlchemy instance

login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
login_manager.init_app(app)

class BLOGS(db.Model):
    # Id : Field which stores unique id for every row in 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=True)
    data = db.Column(db.Text, unique=False, nullable=False)
    # date_added
    # date = db.Column(db.Date, default=db.CURRENT_TIMESTAMP) in flask_postgresql
    # repr method represents how one object of this datatable will look like
    def __repr__(self):
        return f"{self.id}). Name : {self.user_id}, title: {self.title}, desc: {self.description}, data: {self.data}"
class USERS(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    userDescription = db.Column(db.String(300), unique=False, nullable=True)
    userPNG = db.Column(db.String(100), unique=False, nullable=True)
    userFollowers = db.Column(db.Integer, unique=False, nullable=True)
    # userFollowers_id = 
    # repr method represents how one object of this datatable will look like
    def __repr__(self):
        return f"{self.id}). Name : {self.userName}, userDescription: {self.userDescription}, userPNG: {self.userPNG}, userFollowers: {self.userFollowers}"

@login_manager.user_loader
def loader_user(user_id):
    try:
        return USERS.query.get(int(user_id))
    except Exception as e:
        print("Error ", e)
        return
 
 
 
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
        p = USERS(userName=userName, userDescription=userDescription, userPNG=userPNG, userFollowers=userFollowers, email=f"{userName}@gmail.com", password=userName)
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
    user = USERS.query.get(id)
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
                    } for i in USERS.query.all()]
    })

@app.route('/api/post', methods=["POST"])
def post():
    user_id = request.form.get("user_id")
    title = request.form.get("title")
    data = request.form.get("data")
    description = request.form.get("description", default=None)

    # create an object of the Profile class of models
    # and store data as a row in our datatable
    if user_id != None and title != '' and data != '':
        p = BLOGS(user_id=user_id, title=title, data=data, description=description)
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
    data = BLOGS.query.get(id)
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
                        'description' : i.description,
                        'data' : i.data
                    } for i in BLOGS.query.all()]
    })
@app.route('/api/md2html', methods=["POST"])
def md2html():
    data = request.get_json()
    md = data.get('md')
    return jsonify({
        'html' : extract_markdown(md)
        })


# utility functions
def Trending():
    if not PRODUCTION_VERSION:
        allBlogs = BLOGS.query.all()
        random.shuffle(allBlogs)
        allBlogs = allBlogs[:6]
        theirUsers = [USERS.query.get(i.user_id) for i in allBlogs]
    else:
        allBlogs = BLOGS.query.random(length=6)
    theirUsers = [USERS.query.get(i.user_id) for i in allBlogs]
    
    posts = [{'url': f'/posts/{b.id}',
              'idx': "{:02}".format(idx+1),
              'title': b.title,
              'date': 'Mar 12, 2024',
              'length': '5 min',
              'author': u.userName,
              'author_url': f'/users/{u.id}',
              'author_img': u.userPNG} for (idx, (b, u)) in enumerate(zip(allBlogs, theirUsers))]
    
    return posts
def TrendingTags():
    tags = ['Programming', 'Data Science', 'Technology', 'Self Improvement', 'Writing', 'Relationships', 'Machine Learning', 'Productivity', 'Politics']
    return tags

def get_img(markdown_text):
    pattern = r"!\[.*?\][ ]*\((.*?)\)"
    match = re.search(pattern, markdown_text)
    return match.group(1) if match else None
def get_sub_title(markdown_text):
    pattern = r"!\[.*?\][ ]*\((.*?)\)"
    markdown_text = re.sub(pattern, '', markdown_text)
    return ' '.join(markdown_text.split()[:25])

def get_posts(chunk_size=16, userid=None):
    """
    user = None => random blogs or tranding blog
    user = userid => get best blog using ai
    """
    if not PRODUCTION_VERSION:
        allBlogs = BLOGS.query.all()
        random.shuffle(allBlogs)
        allBlogs = allBlogs[:chunk_size]
    else:
        allBlogs = BLOGS.query.random(length=chunk_size)
    theirUsers = [USERS.query.get(i.user_id) for i in allBlogs]
    
    if userid is None:
        posts = [{'url': f'/posts/{b.id}',
                  'title': b.title,
                  'subtitle': b.description if b.description else get_sub_title(b.data),
                  'img': get_img(b.data),
                  'date': 'Mar 12, 2024',
                  'length': '5 min',
                  'author': u.userName,
                  'author_url': f'/users/{u.id}',
                  'author_img': u.userPNG} for b,u in zip(allBlogs, theirUsers)]
    else:
        posts = [{'url': f'/posts/{b.id}',
                  'title': b.title,
                  'subtitle': b.description if b.description else get_sub_title(b.data),
                  'img': get_img(b.data),
                  'tag': 'Hardware',
                  'tag_url': f'/tags/{b.id}',
                  'date': 'Mar 12, 2024',
                  'length': '5 min',
                  'author': u.userName,
                  'author_url': f'/users/{u.id}',
                  'author_img': u.userPNG} for b,u in zip(allBlogs, theirUsers)]
    return posts
    
@app.route('/api/posts', methods=["POST"])
def more_posts():
    data = request.get_json()
    userid = data.get('userid')
    return jsonify({
        'posts' : get_posts(userid=userid, chunk_size=16)
    })



@app.route('/posts/<int:id>')
def blogPage(id):
    data = BLOGS.query.get(id)
    if data:
        user = USERS.query.get(data.user_id) if data.user_id else None
        b = blog(user=user.userName if user else None,
            userPNG=user.userPNG if user else None,
            userFollowers=user.userFollowers if user else None,
            userDescription=user.userDescription if user else None,
            title=data.title,
            subtitle=data.description,
            post_date='Sep 28',
            read_time='18 min',
            reactions={
                'claps': '51',
                'Responds': '1'
            },
            tags=['Machine Learning', 'Deep Learning', 'Data Science', 'Artificial Intelligence', 'Python'])
        b.add(extract_markdown(data.data))
        
        return render_template('blog.html' if current_user.is_authenticated else 'blogNewUser.html', 
                               title=b.title,
                               headingHTML = b.getHeadingHTML(),
                               contentHTML = b.html, 
                               rootFooterHTML = b.getRootFooterHTML(),
                               data=b.html)
    else: 
        return "404 not found"

@app.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('home.html', posts=get_posts(chunk_size=16, userid=current_user.id), userid=current_user.id) # , data='<div>'+''.join([f'<div><a href="/{i.id}">{i.title}</a></div>' for i in BLOGS.query.all()])+'</div>'
    else:
        return render_template('newUser.html', trending=Trending(), trendingTags=TrendingTags(), home_posts=get_posts(chunk_size=16))

#TODO save password sha-256
@app.route('/login', methods=["GET", "POST"])
def login(): 
    if request.method == "POST":
        data = request.get_json()
        try:
            remember = True if data['remember'] else False
            user = USERS.query.filter_by(email=data['email']).first()
            # if not user or not check_password_hash(user.password, password):
            if not user or not (user.password == data['otp']):
                return jsonify({
                    'ok': False,
                })
            else:
                login_user(user, remember=remember)
                return jsonify({
                    'ok': True,
                })
        except Exception as e:
            print("Error ", e)
            return jsonify({
                'ok': False,
            })
            
    return render_template('login.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = request.get_json()
        try:
            user = USERS(userName=data['username'],
                     email=data['email'],
                     password=data['otp'])
            db.session.add(user)
            db.session.commit()
            return jsonify({
                'ok': True,
            })
        except Exception as e:
            print("Error ", e)
            return jsonify({
                'ok': False,
            })
    return render_template('signup.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/new-story', methods=["GET", "POST"])
def write():
    if request.method == "POST":
        data = request.get_json()
        try:
            print(data)
            title = data['title']
            if title == '': raise ValueError("Empty title")
            tags = data['tags']
            description = data['subtitle']
            user_id = data['userid']
            p = BLOGS(user_id=user_id, title=title, data=data['data'], description=description)
            db.session.add(p)
            db.session.commit()
            return jsonify({
                'OK':True
            }) 
        except Exception as e:
            print("Error ", e)
            return jsonify({
                'ok': False,
            })
    username = None if current_user.is_authenticated == False else current_user.userName
    userimg = None if current_user.is_authenticated == False else current_user.userPNG
    userid = None if current_user.is_authenticated == False else current_user.id
    return render_template('new-story.html', is_authenticated = current_user.is_authenticated, username = username, userimg = userimg, userid=userid)

def resetDatabase():
    print("Database reset...")
    if PRODUCTION_VERSION == True:
        db.create_all()
    else:
        os.remove(os.path.join('database', os.listdir('database')[0]))
if not PRODUCTION_VERSION and not os.path.exists(os.path.join(basedir, 'database\\database.db')):
    print('creating database ...')
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    if RESET: resetDatabase()
    app.run(debug=DEBUG, host='0.0.0.0', port=5000)
