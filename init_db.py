import os
import psycopg2
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Access the environment variables
hostname = os.getenv("db_hostname")
port = int(os.getenv("db_port"))
database = os.getenv("db_database")
username = os.getenv("db_username")
password = os.getenv("db_password")
# Construct the connection string
connection_string = f"dbname={database} user={username} password={password} host={hostname} port={port}"
conn = psycopg2.connect(connection_string)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS blogs;')
cur.execute('CREATE TABLE blogs (id serial PRIMARY KEY,'
                                 'user_id integer NOT NULL,'
                                 'title varchar (100) NOT NULL,'
                                 'description varchar (200),'
                                 'data text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                 'userName varchar (20) NOT NULL,'
                                 'userDescription varchar (300) NOT NULL,'
                                 'userPNG varchar (50) NOT NULL,'
                                 'userFollowers integer NOT NULL);'
                                 )

# Insert data into the table

# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('A Tale of Two Cities',
#              'Charles Dickens',
#              489,
#              'A great classic!')
#             )


# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('Anna Karenina',
#              'Leo Tolstoy',
#              864,
#              'Another great classic!')
#             )

conn.commit()

cur.close()
conn.close()