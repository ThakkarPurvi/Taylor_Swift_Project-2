from flask import Flask, request
import requests
import json
import base64
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL,AUTH_URL, SCOPE, SCOPE2, SPOTIFY_REDIRECT_URI, TOKEN


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Automated Taylor Swift Playlist'

@app.route('/spotifycallback', methods=["GET"])
def spotifycallback():
    code = request.args.get('code')
    state = request.args.get('state')
    auth = {'code': code, 'state': state}
    return auth

@app.route('/test', methods=["GET"])
def test():
    return(request.args.get("name"))

if __name__ == '__main__':
    app.run()