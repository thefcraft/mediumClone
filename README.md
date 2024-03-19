# Medium Clone

A Medium clone website built using Flask, PostgreSQL, [flask_pgsql](https://github.com/thefcraft/flask_postgresql), and Flask-Login.

## TODO
At this time for login username and email are same and code(otp) is just password for login

## Features

- **User Authentication:** Users can sign up, log in, and log out securely using Flask-Login.
- **Blog Post Creation:** Authenticated users can create, edit, and delete their own blog posts.
- **Browse and Read Articles:** Users can browse through a list of articles and read them.
- **Responsive Design:** The website is designed to be responsive and accessible on various devices.

## Technologies Used

- **Flask:** A lightweight web framework for Python.
- **PostgreSQL:** A powerful open-source relational database management system.
- **Flask-Login:** Provides user session management for Flask applications.
- **Flask-PGSQL:** My custom API framework for PostgreSQL interactions.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/thefcraft/mediumClone.git
    cd medium-clone
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    # Or
    venv\Scripts\activate  # For Windows
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    - Create a PostgreSQL database.
    - Update the database configuration in `config.py`.

5. **Run the application:**

    ```bash
    python app.py
    ```

6. **Access the application:**

    Open your web browser and go to `http://localhost:5000`.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
