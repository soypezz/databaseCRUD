from flask import Flask, render_template, request, redirect
import cx_Oracle
from DATA import db_user, db_password, db_dsn, db_encoding 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hijo.html')
def hijo():
    
    with cx_Oracle.connect(
            user=db_user,
            password=db_password,
            dsn=db_dsn,
            encoding=db_encoding
        ) as conn:
        cursor = conn.cursor()
        cursor.execute("select * from hijo")
        data = cursor.fetchall()
        headings = [row[0] for row in cursor.description]
    
    return render_template("hijo.html", headings=headings, data=data)

@app.route('/padre.html')
def padre():
    return render_template("padre.html")