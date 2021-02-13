import flask
from flask import request, jsonify
from flask_cors import CORS
from threading import Thread
# from myfolder.myfile import myfunc

# https://github.com/ahampriyanshu/gonewz
app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return '''Yeah side side side project from @BuckthornDev'''

def run():
    app.run()

server = Thread(target=run)
server.start()
