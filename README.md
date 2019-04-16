# Project Name: The Easy CookBook

I decided to use the sample brief given to students for the project to create a web application that allows users to store and easily access cooking recipes.
I used Mongodb as the backend database as the previous course tutorial using pymongo used this NoSql database engine and my project builds upon the course
tutorial adding extra functionality.

The project developed should allow users to 

* Search and display recipes by different criteria
* Add, edit update and delete a recipe on the site , preforming CRUD operations.
* Display a single detailed recipe page
* Optional register and login functionality to allow a user to track their own recipes.
* Design a backend database to group recipes by attributes such as Cuisine, Country, Ingredients

* Project has been published to the Heroku website https://easy-cookbook.herokuapp.com/
* The github repository is located at <a href="https://github.com/desflaherty/milestoneproject3">Github CookBook</a>

## UX

*Strategy:*
The intention for this project would be to create a recipe cookbook that is responsive and visually appealing and uses the frameworks and technologies covered thus
far in the course.

*User Stories:*
As a user of the recipe cookbook I should be able to:
* Browse a listing of all recipes and click into a detailed view of each recipe
* Filter the recipes by searching using different criteria such as Cuisine, Course, Occasion, Special Diet 
* Filter the recipes by searching using a keyword value that would find an ingredient or food type
* Be able to register and login to the site using a username and password that I have supplied
* On login be able to add recipes to the site and view all the recipes I have created
* Be able to preform CRUD operations while I am logged in such as Adding, Editing, Updating and Deleting my recipe.
* Be able to view a detailed page of the recipe to include cooking time, ingredients and instrucitons with an optional image displayed

A mockups for the proposed cookbook can be viewed on githib 
<a href="https://github.com/desflaherty/milestoneproject3/tree/master/Wireframes">Wireframes</a>

## Existing Features

*Header and Footer*
* A navigation bar is displayed with a logo which links to the homepage
* Links are displayed on the right hand side of the navigation menu to allow for browsing of recipes or registration
* On mobile or iPad view the navigation bar will collapse to display a tiled dropdown menu to the right of the navigation.
* A sticky footer is displayed through the website.

*Index*
* This is the homepage displaying a background image
* On desktop a message is displayed to inform the user they can browse or register to create a recipe
* On mobile the message is removed as it is not as visually appealing
* 'Enter' and 'Register' buttons are displayed in the center of the homepage

*Register & Login*
* A user can create an account and choose a username. 
* A password is chosen which is hashed in the database for security
* There is a form control implemented where a chosen password and confirmation password must match
* This username will be used to log in and identify a recipe belonging to that user

*Profile*
* Displays the username and a welcome message when the user has logged into the site

*Recipes*
* A user can browse all recipes in the cookbook.
* A search menu is displayed where the user can filter recipes by choosing from dropdown menus - Cuisine, Course, Special Diet
* An input box is available where the user can perform a text search
* Search features can be combined or just one search option can be chosen

*Filter_Recipes*
* This page returns the search results when I user uses the search menu to filter recipes
* A count of filtered recipes is displayed

*My Recipes*
* Where a user has logged into the site and has added a recipe
* A counter displays the number of recipes that the user has created

*Single Recipe*
(This page displays a detailed view of each recipe)
* Recipe name, preparation time, cooking time, serving, ingredients, cooking instructions
* An image is displayed
* The cuisine type, course type and diet are highlighted

*My Single Recipe*
(This page is for users that have registered and have logged in)
* A detailed view of the recipe is displayed
* Users also have the option to edit or delete the recipe

*Add and Edit Recipe*
* These pages have the form inputs for the information of the recipe the user is adding or editing.
* HTML form input validation is used so that mandatory fields must be populated

*Delete Recipe*
* When a user creates a recipe they can also delete it
* A popup modal is used to display a message to the user to confirm delete


## Technologies, Programming Languages and Frameworks

*Python*
* Controls functionality of the project
* https://www.python.org

*MongoDB*
* Backend NoSql database which contains the schema used in the project
* All data displayed through the front end is stored here
* Inputted data from user is stored in recipe & user tables
* https://www.mongodb.com

*Pymongo*
* Contains script for interacting with MongoDB database from Python
* https://api.mongodb.com/python/current

*JQuery*
* Used for form creation
* Navigation collapse for mobile view
* Modal popup for delete confirmation
* Form validation for dropdown menus
* Password match validation on register & login forms

*Materialize*
* A responsive front end-framework based on material design 
* http://archives.materializecss.com/0.100.2

*Jinja*
* Implement python code into html 5

*Flask*
* Redirecting and rendering of page route through python
* http://flask.pocoo.org

*HTML 5*
* Positioning and format of html elements.
* https://www.w3schools.com/html/default.asp

*CSS3*
* Styling the HTML elements
* https://www.w3schools.com/css/

*Font Awesome*
* Icons used in the single recipe page to cooking time
* https://fontawesome.com/

*Google Font*
* Font 'Abel' used throughout the site
* href=//fonts.googleapis.com

*Amazon web services*
* AWS S3 bucket services were used to create a bucket where images for the recipes could be stored
* The URL path to these images were then added to the respective recipe in the Mongo database

## Testing

<a href="https://github.com/desflaherty/milestoneproject3/blob/master/Manual_testing.md">Manual Testing</a>

## Testing Issues
* On FireFox the CSS overwriting the grey text default to black for materialize text input box in the search ingredients menu does not work.  
* Flash messages that should appear during the login and register process are not firing


## Features left to implement
* Recipe likes were manually added to the database for this project. For the next milestone project a counter will be developed to track likes by registered users.
* A view count could be implemented to track the number of times a recipe page was viewed
* Further validation control could be implemented on user login and register to provide feedback to the user 
* Custom form validation could be added using Javascript, currently HTML validation is used
* The design of the database schema could be further improved to add functionality for tracking user activity on the website
* Ingredients in the single recipe page could be displayed in bullet format using programming logic

## Validation
* HTML:Checked with W3C validator. Only Jinja related errors due to the validation not programmed these
* CSS:Checked with CSS lint. No errors were displayed
* Python: PEP8 was used to check code for any major errors

## Database Schema

### There are 7 Collections in the Mongo database schema

![picture](static/images/testing/mongo_schema.jpg)

* In the Cuisine,Course,Occasion,Skill and Special_Diets collections are created using 'name, value pairs'

![picture](static/images/testing/cuisine_collection.jpg)

* The dropdown menu items used in the search form are built from the collections mentioned above - Cuisine,Course,Skill,Special_Diets
* Each object in these collections has a unique object id which is the primary key in the collection
* The User_Details collection contains the user details that are entered through the front end form in the app with a hashed password
* The Recipe collection contains the foreign keys from the Cuisine, Course, Occasion, Skill, Special_Diets collections and username
* The Recipe collection contains all details used to display the recipe in the single recipe page on the site
* Username in the Recipe collection is added when the user creates a recipe after they login to the website

![picture](static/images/testing/user_in_db.jpg)
![picture](static/images/testing/recipe_in_db.jpg)



## Deployment
*Deployment to Heroku*
* Created a new app called easy-cookbook
* heroku login Entered username and password.
* git init to initialise a git repository.
* git remote add heroku https://easy-cookbook.herokuapp.com/ to link the GitHub repository to the Heroku app.
* pip3 freeze --local > requirements.txt Creates a .txt file which tells Heroku what dependencies the project is using.
* echo web: python run.py >procfile Tells Heroku that this project is a web app and that "app.py" is going the run it.
* ps:scale web=1
*Set config variables in the app.py file so Heroku can find them*
* app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
* app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
* app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
*Push to Heroku in the command terminal*
* git add
* git commit -m "message"
* git push heroku master pushes the project to Heroku.
*Heroku config variables*
* In Heroku set config variables
* IP = `0.0.0.0`
* PORT =  `8080`
* SECRET_KEY = |secret key|
* MONGO_DBNAME = |database name|
* MONGO_URI = mongodb://|username|:|password|@xxxxxxxxxxxxxx/|database name|

* Project deployed https://easy-cookbook.herokuapp.com/

*Running code locally*
* git clone https://github.com/desflaherty/milestoneproject3
* sudo pip3 install flask
* sudo pip3 install pymongo
* sudo pip3 install flask_pymongo
* setup a database in mongo db 
* setup a username and password for the database
* Take note of the MongoDB URI after creating a user e.g mongodb://|yourusername|:|yourpassword|@mongodb.net/|yourdatabasename
* create collections needed for cuisine, course, occasion, diet, recipe, skill, user details
* In the project folder create a config.py file
* In the terminal line enter echo 'config.py' > gitignore to hide the config.py file
* In the config.py file enter the following:
   *DB_CONFIG={   
   *'MONGO_DBNAME':'databasename',
   *'MONGO_URI':'mongodb+srv://password/cluster-lgqe5.mongodb.net/databasename',
   *'SECRET_KEY':"secret key"
   *}
* In app.py, set the app.config variables to the variables set in the config.py file
    *import config
    *app.secret_key = config.DB_CONFIG['SECRET_KEY']
    *app.config["MONGO_DBNAME"] = config.DB_CONFIG['MONGO_DBNAME']
    *app.config["MONGO_URI"] = config.DB_CONFIG['MONGO_URI']
*In the terminal run python3 app.py to run the app


## Credits

### Data
* The recipe information used for the project was sourced online from http://www.foodnetwork.co.uk/recipes.html
* The background image for the site was sourced from https://unsplash.com

### Code
* The session register and login code used in the app.py file was sourced from a fellow student MIROSLAV SVEC as referenced in the file
* https://materializecss.com was used for the navigation framework 
* The code used to fire HTML validation for the dropdown menus was sourced from stack overflow - https://stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown/40124502
* The code for the modal delete confirmation was sourced from materialize https://materializecss.com/modals.html
* Jquery code used for password match was sourced https://gist.github.com/grayghostvisuals/6984561



