In this project, you’ll be building a data-driven web application using the technologies that you have learned throughout Data Centric Development. You can either choose to to follow the example brief below, or you can use your own idea for the website.

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
https://github.com/desflaherty/milestoneproject3/tree/master/Wireframes

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
This page displays a detailed view of each recipe
* Recipe name, preparation time, cooking time, serving, ingredients, cooking instructions
* An image is displayed
* The cuisine type, course type and diet are highlighted

*My Single Recipe*
This page is for users that have registered and have logged in
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

## Testing

*Manual Testing*


