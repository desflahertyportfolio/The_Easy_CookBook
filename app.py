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


   
@app.route('/cuisine')
def cuisine():
    return render_template("cuisine.html", cuisine=mongo.db.Cuisine.find())    
 
    
@app.route('/recipes')
def recipes():
    return render_template("recipes.html",recipe=mongo.db.Recipe.find(),cuisine=mongo.db.Cuisine.find(),course=mongo.db.Course.find(),diet=mongo.db.Special_Diets.find()) 
                            
  
@app.route('/single_recipes/<recipe_id>')
def single_recipes(recipe_id):
    the_recipe =  mongo.db.Recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template("singlerecipe.html",
                            recipe=the_recipe)  
    
    
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
    
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.Recipe.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines =  mongo.db.Cuisine.find()
    all_courses =  mongo.db.Course.find()
    all_occasions =  mongo.db.Occasion.find()
    all_diets =  mongo.db.Special_Diets.find()
    all_skills =  mongo.db.Skill.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           cuisine=all_cuisines,course=all_courses,
                           occasion=all_occasions,diet=all_diets,skill=all_skills)
                           
                           
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.Recipe
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_description':request.form.get('recipe_description'),
        'cuisine_name':request.form.get('cuisine_name'),
        'course_name':request.form.get('course_name'),
        'occasion_name':request.form.get('occasion_name'),
        'diet_name':request.form.get('diet_name'),
        'skill_name':request.form.get('skill_name'),
        'ingredients':request.form.get('ingredients'),
        'cook_time':request.form.get('cook_time'),
        'prep_time':request.form.get('prep_time'),
        'serves':request.form.get('serves'),
        'instruction_step_1':request.form.get('instruction_step_1'),
        'instruction_step_2':request.form.get('instruction_step_2'),
        'instruction_step_3':request.form.get('instruction_step_3'),
        'instruction_step_4':request.form.get('instruction_step_4'),
        'instruction_step_5':request.form.get('instruction_step_5'),
        'instruction_step_6':request.form.get('instruction_step_6'),
        'image':request.form.get('image'),
        'author':request.form.get('author')
    })
    return redirect(url_for('recipes'))  
    

@app.route('/delete_recipe/<recipe_id>', methods=["POST"])
def delete_recipe(recipe_id):
    mongo.db.Recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipes'))    
 
 
                            
                             
@app.route('/filter_recipes_cuisine', methods=["GET", "POST"])
def filter_recipes_cuisine():
    cuisine = mongo.db.Cuisine.find()
    course = mongo.db.Course.find()
    if request.method == "POST":
        cuisine = request.form.get('cuisine_name')
        course = request.form.get('course_name')
        recipes= mongo.db.Recipe.find({"cuisine_name" :cuisine})
        #recipes= mongo.db.Recipe.find({"course_name" :course})
        #recipes= mongo.db.recipes.aggregate([{"$match" :{"$and": [{ "course_name" : course }, { "cuisine_name" : cuisine }]   }}])
        return render_template ('filter_recipes.html', recipe=recipes,cuisine=cuisine)
    else:
        recipes = mongo.db.Recipe.find()
        return render_template('recipes.html', recipe=recipes, cuisine=cuisine)

@app.route('/filter_recipes_course', methods=["GET", "POST"])
def filter_recipes_course():
    cuisine = mongo.db.Cuisine.find()
    course = mongo.db.Course.find()
    if request.method == "POST":
        cuisine = request.form.get('cuisine_name')
        course = request.form.get('course_name')
        recipes= mongo.db.Recipe.find({"course_name" :course})
        return render_template ('filter_recipes.html', recipe=recipes,course=course)
    else:
        recipes = mongo.db.Recipe.find()
        return render_template('recipes.html', recipe=recipes, course=course)





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)