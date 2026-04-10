"""
Cloud Infrastructure Setup - Python Web Application
Deployed on AWS EC2 using Docker and MySQL
Author: Harivasanth Arava
"""

from flask import Flask, render_template_string, jsonify
import mysql.connector
import os

app = Flask(__name__)

DB_CONFIG = {
    'host':     os.environ.get('DB_HOST', 'localhost'),
    'user':     os.environ.get('DB_USER', 'harivasanth'),
    'password': os.environ.get('DB_PASSWORD', 'hari123'),
    'database': os.environ.get('DB_NAME', 'myappdb')
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AWS Cloud App</title>
    <style>
        body { font-family: Arial; background: #080d0a;
               color: white; text-align: center; padding: 60px; }
        h1 { color: #3dba6a; font-size: 38px; }
        .card { background: #0f2016; border: 1px solid #2a6a3a;
                border-radius: 10px; padding: 20px;
                margin: 16px auto; max-width: 500px; }
        .badge { background: #1a4025; padding: 8px 16px;
                 border-radius: 6px; margin: 6px;
                 display: inline-block; color: #3dba6a; }
    </style>
</head>
<body>
    <h1>☁️ AWS Cloud Infrastructure - Live!</h1>
    <div class="card">
        <p>Deployed on <strong>AWS EC2</strong> using Docker</p>
        <div class="badge">🐧 Linux Ubuntu</div>
        <div class="badge">🐳 Docker</div>
        <div class="badge">🗄️ MySQL</div>
        <div class="badge">🐍 Python Flask</div>
        <div class="badge">☁️ AWS EC2</div>
    </div>
    <div class="card">
        <h3>Database Status</h3>
        <p>{{ db_status }}</p>
    </div>
    <p>By <strong>Harivasanth Arava</strong> |
       MCA Cloud Computing | Jain University</p>
</body>
</html>
"""

@app.route('/')
def home():
    db_status = "❌ Database not connected"
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        db_status = "✅ MySQL Connected Successfully!"
        conn.close()
    except Exception as e:
        db_status = f"❌ DB Error: {str(e)}"
    return render_template_string(HTML_TEMPLATE, db_status=db_status)

@app.route('/health')
def health():
    return jsonify({"status": "running", "author": "Harivasanth Arava"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
