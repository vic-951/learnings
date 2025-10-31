from flask import Flask, render_template, request, redirect, url_for, jsonify, session, send_from_directory
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import sqlite3
import os
from datetime import timedelta
import logging

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'fallback_jwt_secret_key')
JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', '3600'))
DATABASE_URL = os.getenv('DATABASE_URL', 'users.db')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
PORT = os.getenv('PORT', 5000)

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=JWT_ACCESS_TOKEN_EXPIRES)
app.config['DEBUG'] = DEBUG

jwt = JWTManager(app)

def init_db():
    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/media/<path:filename>')
def media_file(filename):
    return send_from_directory('media', filename)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        hashed_password = generate_password_hash(password)
        
        try:
            conn = sqlite3.connect(DATABASE_URL)
            c = conn.cursor()
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                     (username, hashed_password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return "Benutzername bereits vergeben!"
        except Exception as e:
            return f"Fehler bei der Registrierung: {str(e)}"
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            conn = sqlite3.connect(DATABASE_URL)
            c = conn.cursor()
            c.execute('SELECT id, username, password FROM users WHERE username = ?', (username,))
            user = c.fetchone()
            conn.close()
            
            if user and check_password_hash(user[2], password):
                access_token = create_access_token(identity=user[0])
                session['access_token'] = access_token
                session['user_id'] = user[0]
                session['username'] = user[1]
                return redirect(url_for('dashboard'))
            else:
                return "Ungültige Anmeldedaten!"
        except Exception as e:
            return f"Fehler bei der Anmeldung: {str(e)}"
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'access_token' not in session:
        return redirect(url_for('login'))
    
    try:
        return render_template('dashboard.html', username=session.get('username'))
    except Exception as e:
        session.clear()
        return redirect(url_for('login'))

@app.route('/api/protected')
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return jsonify(logged_in_as=current_user_id)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
def index():
    return redirect(url_for('login'))

init_db()

@app.errorhandler(404)
def not_found_error(error):
    return "Seite nicht gefunden", 404

@app.errorhandler(500)
def internal_error(error):
    return "Interner Serverfehler", 500

if __name__ == '__main__':
    print(f"  Debug: {DEBUG}")
    
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)