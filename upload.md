# Flask PostgreSQL Library

The Flask PostgreSQL library provides a convenient interface for integrating PostgreSQL databases into Flask applications. This library simplifies database interactions by offering an easy-to-use API similar to Flask-SQLAlchemy.

## Installation

> Install the following

You can install the Flask PostgreSQL library using pip:

```bash
pip install flask-postgresql
```

## Usage

### Initialization

To initialize the PostgreSQL connection, import the `PostgreSQL` class from `flask_postgresql` and provide the necessary connection parameters:

```python
import os
from flask_postgresql import PostgreSQL

# Retrieve database connection parameters from environment variables
hostname = os.getenv("db_hostname")
port = int(os.getenv("db_port"))
database = os.getenv("db_database")
username = os.getenv("db_username")
password = os.getenv("db_password")

# Initialize the PostgreSQL connection
db = PostgreSQL(hostname=hostname, port=port, database=database, username=username, password=password)
```

### Defining Models

Define your database models by subclassing `db.Model`. Here's an example of defining `BLOGS` and `USERS` models:

```python
class BLOGS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    data = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"{self.id}). Name : {self.user_id}, title: {self.title}, description: {self.description}, data: {self.data}"

class USERS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(20), nullable=False)
    userDescription = db.Column(db.String(300), nullable=False)
    userPNG = db.Column(db.String(50), nullable=False)
    userFollowers = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.id}). Name : {self.userName}, userDescription: {self.userDescription}, userPNG: {self.userPNG}, userFollowers: {self.userFollowers}"
```

### Querying Data

You can perform database queries using the models defined above, just like with Flask-SQLAlchemy:

```python
# Query all blogs
all_blogs = BLOGS.query.all()

# Query all users
all_users = USERS.query.all()
```

### Additional Features

The Flask PostgreSQL library supports additional features such as adding, updating, and deleting data, as well as executing raw SQL queries. Refer to the documentation for more information.

## Contributing

Contributions to the Flask PostgreSQL library are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README to include more details or additional sections specific to your project's needs.