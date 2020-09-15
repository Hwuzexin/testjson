import os
import json

from flask import Flask, flash, redirect, render_template, \
    request, url_for

app = Flask(__name__)
app.secret_key = os.urandom(8)


def caljson(aaa):
    getjson = json.loads(aaa)
    getoutcome = getjson
    return getoutcome


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


@app.route('/login', methods=['GET', 'POST'])
def login():
    sta = None
    if request.method == 'POST':
        sta = request.form['username']
    print(type(sta))
    if sta:
        if is_json(sta):
            staa = caljson(sta)
            for key in staa:
                print(key, staa[key])
    return render_template('login.html', outcome=sta)


if __name__ == '__main__':
    app.run()