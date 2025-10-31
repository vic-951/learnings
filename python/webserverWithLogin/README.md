# Description
This is a complete web application built with Python Flask that provides user authentication with login and registration functionality, JWT-based security, and a personalized dashboard with custom image display.
You can use it for simple projects in your homelab. **Please don´t use it for sensible informations or make it accessible from the internet**. I was just learning a bit and don´t implementet much security features.
# How to use
## Create .env
Create a .env file in root folder.
```
# Secrets
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_secret_key

# Configuration
JWT_ACCESS_TOKEN_EXPIRES=3600
DEBUG=True
PORT=5000

# Database
DATABASE_URL=users.db
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
## Create virtual invironment
```
cd webserverWithLogin
python3 -m venv venv
venv\Scripts\activate # On Windows
source venv/bin/activate # On MacOS
pip install -r requirements.txt
```
## Start app
In your virtual invironment
```
python3 app.py
```