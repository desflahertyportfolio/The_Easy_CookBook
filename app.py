import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
import pymongo

from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] ='CookBook'
app.config["MONGO_URI"] ='mongodb+srv://root:Allergan99@myfirstcluster-lgqe5.mongodb.net/CookBook'

"""
app.debug = False
if app.debug == True:
    import config
    app.config["MONGO_DBNAME"] = config.DB_CONFIG['MONGO_DBNAME']
    app.config["MONGO_URI"] = config.DB_CONFIG['MONGO_URI']
else:
    app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
"""

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/recipes')
def recipes():
    return render_template("recipes.html")
   
@app.route('/cuisine')
def cuisine():
    return render_template("cuisine.html", cuisine=mongo.db.Cuisine.find())    
    
    
    
    
@app.route('/add_recipes')
def add_recipes():
    return render_template('addrecipe.html',
    cuisine=mongo.db.Cuisine.find(),
    course=mongo.db.Course.find(),
    occasion=mongo.db.Occasion.find(),
    diet=mongo.db.Special_Diets.find(),
    skill=mongo.db.Skill.find()
    )
   
  
    
    
    
    
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe =  mongo.db.Recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))    
    
 


    
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)