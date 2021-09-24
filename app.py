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
    
    with cx_Oracle.connect(
            user=db_user,
            password=db_password,
            dsn=db_dsn,
            encoding=db_encoding
        ) as conn:
        cursor = conn.cursor()
        cursor.execute("select * from padre")
        data = cursor.fetchall()
        headings = [row[0] for row in cursor.description]
    
    return render_template("padre.html", headings=headings, data=data)

@app.route('/consulta1.html')
def consulta1():
    
    return render_template("consulta1.html")

@app.route('/consulta2.html')
def consulta2():
    
    return render_template("consulta2.html")

@app.route('/consulta3.html')
def consulta3():
    
    return render_template("consulta3.html")

@app.route('/consulta4.html')
def consulta4():
    
    return render_template("consulta4.html")