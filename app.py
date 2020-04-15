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
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_animals')
def get_animals():
    return render_template("animals.html", animals=mongo.db.animals.find())


@app.route('/add_animal')
def add_animal():
    return render_template("addanimal.html", group=mongo.db.group.find())


@app.route('/insert_animal', methods=['POST'])
def insert_animal():
    animals = mongo.db.animals
    animals.insert_one(request.form.to_dict())
    return redirect(url_for('get_animals'))


@app.route('/update_animal/<animal_id>')
def edit_animal(animal_id):
    the_animal = mongo.db.animals.find_one({"_id": ObjectId(animal_id)})
    all_groups = mongo.db.group.find()
    return render_template('editanimal.html',
                           animal=the_animal, group=all_groups)


@app.route('/update_animal/<animal_id>', methods=['POST'])
def update_animal(animal_id):
    animals = mongo.db.animals
    animals.update({'_id': ObjectId(animal_id)},
                   {
        'animal_name': request.form.get('animal_name'),
        'child_name': request.form.get('child_name'),
        'group_name': request.form.get('group_name'),
        'diet': request.form.get('diet'),
        'habitat': request.form.get('habitat'),
        'animal_image': request.form.get('animal_image')
    })
    return redirect(url_for('get_animals'))


@app.route('/delete_animal/<animal_id>')
def delete_animal(animal_id):
    mongo.db.animals.remove({'_id': ObjectId(animal_id)})
    return redirect(url_for('get_animals'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
