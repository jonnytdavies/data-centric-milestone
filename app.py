import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "myProjectDB"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_animals')
def get_animals():
    return render_template("animals.html", animals=mongo.db.animals.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
