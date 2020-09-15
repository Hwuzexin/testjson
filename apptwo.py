import os
import json

import pandas as pd
from pandas import DataFrame
from flask import Flask, flash, redirect, render_template, \
    request, url_for

app = Flask(__name__)
app.secret_key = os.urandom(8)


def caljson(aaa):
    getjson = json.loads(aaa)

    return getjson


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

def count(staa):
    num = 0
    for key in staa:
        for i in staa[key]:
            num += i
    return num


def test(sta):
    if sta:
        if is_json(sta):
            staa = caljson(sta)
            for key in staa:
                print(key, staa[key])
                print(type(key))
                print(type(staa[key]))
            staa = count(staa)
            return staa
        else:
            return "请输入正确的json数据"


@app.route('/count', methods=['GET', 'POST'])
def login():
    sta = None
    if request.method == 'POST':
        sta = request.form['username']
    print(type(sta))
    staa = test(sta)
    return render_template('login.html', outcome=staa)


if __name__ == '__main__':
    app.run()