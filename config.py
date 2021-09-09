from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['TEMPLATES-AUTO-RELOAD'] = True
