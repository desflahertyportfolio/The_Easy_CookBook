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
    if request.method == "POST":
        cuisine = request.form.get('cuisine_name')
        recipes= mongo.db.Recipe.find({"cuisine_name" :cuisine})
        #recipes= mongo.db.Recipe.find({"course_name" :course})
        #recipes= mongo.db.recipes.aggregate([{"$match" :{"$and": [{ "course_name" : course }, { "cuisine_name" : cuisine }]   }}])
        return render_template ('filter_recipes.html', recipe=recipes,cuisine=cuisine)
    else:
        recipes = mongo.db.Recipe.find()
        return render_template('recipes.html', recipe=recipes, cuisine=cuisine)

@app.route('/filter_recipes_course', methods=["GET", "POST"])
def filter_recipes_course():
    course = mongo.db.Course.find()
    if request.method == "POST":
        course = request.form.get('course_name')
        recipes= mongo.db.Recipe.find({"course_name" :course})
        return render_template ('filter_recipes.html', recipe=recipes,course=course)
    else:
        recipes = mongo.db.Recipe.find()
        return render_template('recipes.html', recipe=recipes, course=course)


@app.route("/find_ingredient", methods=["GET", "POST"])
def find_ingredient():
   if request.method == "POST":
      mongo.db.Recipe.create_index([("$**", "text")])
      ingredients=request.form.get('ingredients')
      recipes= mongo.db.Recipe.find({"$text": {"$search": ingredients }})
      return render_template('filter_recipes.html',recipe=recipes,ingredients=ingredients)
   else:
        recipes = mongo.db.Recipe.find()
        return render_template('recipes.html', recipe=recipes, ingredients=ingredients)
 

@app.route("/find_multiple_categories", methods=["GET", "POST"])
def find_multiple_categories():
    cuisine = mongo.db.Cuisine.find()
    course = mongo.db.Course.find()
    diet=mongo.db.Special_Diets.find()
    if request.method == "POST":
       ingredients = request.form.get("ingredients")
       cuisine = request.form.get("cuisine_name") 
       course = request.form.get("course_name")
       diet=request.form.get("diet_name")
       mongo.db.Recipe.create_index([("$**", "text")])
       recipes= mongo.db.Recipe.find({"$text": {"$search": ingredients }})
       
       
       
       
       if course and not cuisine and not ingredients and not diet:
         recipes= mongo.db.Recipe.find({"course_name" :course})
         
       elif cuisine and not course  and not ingredients and not diet:
         recipes= mongo.db.Recipe.find({"cuisine_name" :cuisine})
         
         
       elif diet and not course and not cuisine and not ingredients:
         recipes= mongo.db.Recipe.find({"diet_name" :diet}) 
         
       elif ingredients and not course and not cuisine and not diet:
            recipes= mongo.db.Recipe.find({"$text": {"$search": ingredients }})
          
          
       elif course and cuisine and not ingredients and not diet:
              recipes = mongo.db.Recipe.find({"$and": [{"cuisine_name": cuisine}, {"course_name": course}] }) 
          
       elif ingredients and cuisine and not course and not diet:
               recipes = mongo.db.Recipe.find({"$and": [{"cuisine_name": cuisine}, {
                                           "$text": {"$search": ingredients }} ] })   
       
       elif ingredients and course and not cuisine and not diet:
               recipes = mongo.db.Recipe.find({"$and": [{"course_name": course}, {
                                           "$text": {"$search": ingredients }} ] })  
       
       elif ingredients and diet and not cuisine and not course:
               recipes = mongo.db.Recipe.find({"$and": [{"diet_name": diet}, {
                                           "$text": {"$search": ingredients }} ] })
                                           
       elif ingredients and diet and cuisine and not course:
               recipes = mongo.db.Recipe.find({"$and": [{"diet_name": diet},{"cuisine_name": cuisine}, {
                                           "$text": {"$search": ingredients }} ] })  
                                           
       elif ingredients and diet and course and not cuisine:
               recipes = mongo.db.Recipe.find({"$and": [{"diet_name": diet},{"course_name": course}, {
                                           "$text": {"$search": ingredients }} ] })                                     
                                           
       
       elif diet and course and cuisine and not ingredients:
              recipes = mongo.db.Recipe.find({"$and": [{"cuisine_name": cuisine}, {"course_name": course}, {"diet_name" :diet} ]})
              
       elif diet and cuisine and not course and not ingredients:
              recipes = mongo.db.Recipe.find({"$and": [{"cuisine_name": cuisine}, {"diet_name" :diet} ]})      
       
       
       elif diet and course and not cuisine and not ingredients:
              recipes = mongo.db.Recipe.find({"$and": [{"course_name": course}, {"diet_name" :diet} ]})  
                                           
       elif ingredients and cuisine and course and not diet:
           recipes = mongo.db.Recipe.find({"$and": [{"cuisine_name": cuisine}, {"course_name": course}, {
                                           "$text": {"$search": ingredients }} ] }) 
                                           
       elif ingredients and cuisine and course and diet:
           recipes = mongo.db.Recipe.find({"$and": [{"cuisine_name": cuisine}, {"course_name": course},{"diet_name" :diet}, {
                                           "$text": {"$search": ingredients }} ] })     
                                           
    recipe_count = recipes.count()                                   
                                           
    return render_template('filter_recipes.html',recipe=recipes,ingredients=ingredients,cuisine=cuisine,course=course,diet=diet,recipe_count=recipe_count)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)