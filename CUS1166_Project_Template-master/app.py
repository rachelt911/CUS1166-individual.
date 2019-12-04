from os import name

import app as app
from app import create_app
from flask import Flask
app = Flask(__name__)

app = create_app()
