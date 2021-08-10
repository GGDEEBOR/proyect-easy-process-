from flask import Flask
from flask import render_template, request
from flask_mysqldb import MySQL


app= Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '3306'
app.config['MYSQL_DB'] = 'flaskcontacts'

mysql = MySQL(app)

from controller import *

if __name__ == '__main__':
    app.run(debug=True) 
