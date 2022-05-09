from flask import Flask, request, render_template
import requests
import json
import base64
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL,AUTH_URL, SCOPE, SCOPE2, SPOTIFY_REDIRECT_URI, TOKEN


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            print("yes")
        elif request.form.get('action2') == 'VALUE2':
            print("no")
        else:
            print("maybe")
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

@app.route('/spotifycallback', methods=["GET"])
def spotifycallback():
    code = request.args.get('code')
    state = request.args.get('state')
    auth = {'code': code, 'state': state}
    return auth

@app.route('/question1', methods=["GET"])
def test():
    return(request.args.get("name"))

@app.route('/question2', methods=["GET"])
def handle_question2():
    pass
"""
    if answer =='ME':
        return redirect(url_for('login'))
    elif answer = "OTHER":
        
    else:
        return redirect(url_for('question3'))
"""
if __name__ == '__main__':
    app.run(debug = True)