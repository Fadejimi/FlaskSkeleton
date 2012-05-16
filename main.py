from __future__ import with_statement # needed for contextlib
from contextlib import closing # needed for init_db

import urllib2
import time, datetime
import sqlite3
import json
import pdb
import csv

from operator import itemgetter

from pprint import pprint

from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash, Response

from jinja2 import Environment, PackageLoader

DATABASE = "skeleton.db"
DEBUG = True
SECRET_KEY = "development key"
USERNAME = "admin"
PASSWORD = "default"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar("SETTINGS", silent=True)

env = Environment(loader=PackageLoader('main', 'templates'))

def connect_db():
    return sqlite3.connect(app.config["DATABASE"])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource("schema.sql") as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False):
    cursor = g.db.execute(query, args)
    rv = [dict((cursor.description[index][0], value) for index, value in enumerate(row)) for row in cursor.fetchall()]
    return (rv[0] if rv else None) if one else rv

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route("/")
def index():
    data = {}
    data["messages"] = query_db("select * from messages")

    # Uncomment to see the json output instead of the html rendering.
    # return Response(json.dumps(data), mimetype="application/json")
    return render_template("home.html", data=data)

@app.route("/addmessage", methods=["POST"])
def add_message():
    db = connect_db()
    db.execute("insert into messages (title, body) values(?, ?)", [request.form["title"], request.form["message"]])
    db.commit()
    db.close()

    return redirect(url_for("index"))

@app.route("/generate")
def generate():
    init_db()
    return "Success"

if __name__ == "__main__":
    app.run()
