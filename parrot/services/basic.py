from flask import g
from parrot import app

@app.route('/')
def home():
    return 'test'
