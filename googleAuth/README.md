## Base Authentication Django APP with JWT Authentication

# Custom Google Authentication System Tutorial Code

This repository contains the code for building a custom Google authentication system using Django Rest Framework and ReactJS. The tutorial is divided into two parts: setting up the backend with Django and implementing the frontend with React.

## Key Features

- **Backend:** Django Rest Framework setup, custom user model, Google OAuth integration

## Getting Started Base Authentication Django APP with JWT Authentication

1. Clone the repository: `https://github.com/cis-muzahid/googla_auth.git`

- cd googleAuth

# Create .env file and update this variables 

- GOOGLE_OAUTH2_CLIENT_SECRET="YOUR_CLIENT_SECRET_ID_CREATED_BY_GOOGLE_CONSOLE"
- GOOGLE_OAUTH2_CLIENT_ID="YOUR_CLIENT_ID_CREATED_BY_GOOGLE_CONSOLE"

# Create- 
- Create a virtual environment to install dependencies in and activate it:


- python3.12 -m venv env_name


- source env_name/bin/activate


- Then install the dependencies:


- (env_name)$ pip install -r requirements.txt


- Note the `(env_name)` in front of the prompt. This indicates that this terminal
- session operates in a virtual environment set up by `virtualenv`.

- Once `pip` has finished downloading the dependencies:

- Migrate the database

- (env_name)$ python manage.py migrate

- Go to the root DIR:

- (env_name)$ python manage.py runserver

- And navigate to `http://127.0.0.1:8000/`.


