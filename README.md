# iSandwich

iSandwich is a Flask and MongoDB web application that helps users to find and share their Sandwich recipes online! This app allows users to get the most out of their passion with both sandwiches and sandwich recipes. With this app they can find new recipes, search ingredients, add new recipes, edit old recipes and delete their own recipes.

## User Experience (UX)

This application is dedicated to all Sandwich lovers out there in the big world, that has been trying for years to find and share their sandwich recipes with others online.

iSandwich help users come together as a community to share their interest and passion for sandwiches.

To be able to build the iSandwich app, I had to include:

A simple way of navigating around the page. Login and sign up page for the users. Showcase photos, information, ingredients and instructions of sandwich and different recipes. Users should be able to add, edit and delete their recipes.

I tried to stay on the same path during the entire project with colors, design and idea.

Mockup for the Project

Link to the iSandwich Mockup made in Figma:

https://www.figma.com/file/VYEOxrCaigUv6gqqvZYQSa/iSandwich?node-id=0%3A1

## Features

Home Page Navbar with easy and readable links. Hero Image - A big sandwich with some welcoming and fun text, that get the sandwich loving users to feel excited. Short description about the page and how to join the community. Links to sign up page.

#### About Page 
Hero Image - of a big and delicious sandwich with sub-text below. Information about the iSandwich history and the great idea behind it.

#### Sandwiches Page 
A big hero image of a sandwich. A nice view of all the sandwiches located in the app’s database. A search bar to search for specific ingredients. A category filter, to filter out different types of sandwiches that exist in the database.

#### Login Page 
Input for both username, password and with a submit button below to login to the page.

#### Sign up Page 
Input for username, password and an unique display name for the user (so that the user does not have to show his username during his/her session time, safety first!) to be able to get an account and login to the page.

#### Profile Page 
Always the starting point for the logged in user and here the users can se their own display_names while logged in. The user can also both edit and delete their Sandwiches on this page.

#### Add Sandwich Page
Here the user can add and build their own recipe of a sandwich that they would like to share with others.

## Technologies used in the project 

Figma,
HTML5, 
CSS, 
Bootstrap, 
JQuery, 
JavaScript, 
Python, 
Pymongo, 
Flask, 
MongoDB, 
Heroku

## Testing 
I have tested the iSandwich website and was unable to find any error or bad links on the website. Devices Used: iPhone x – iOS 11.4 iPad – iOS 11.2.2 & iOS 11.4.1 MacBook – iOS 11.4 PC – Windows 10 Browsers Used: Chrome Firefox Safari

## Issues/problems/improvements 

No known bugs or bigger problems, however some things should be fixed for a 2.0 version:

The search function could improve a lot... You only search for specific string at the moment. This is what happens when you run out of time before a deadline.

Show the display name of which user that has created the recipe.

An allergens button to the Sandwich page, to be able to filter allergens faster.

An file upload function instead in the "add sandiwch" page. The solution for this is about 90% done. Will be un-commentend in the next version. 

## Validation HTML 
All files passed validation at https://validator.w3.org/nu/#textarea

## Version Control

#### Git
I have used Git as a version control system to regularly add and commit changes made to project in Gitpod IDE, before pushing them into GitHub.

#### GitHub
I have used GitHub as a remote repository to add and store the committed changes to my project from Git.

## Hosting Heroku
I have used Heroku as the hosting platform to deploy the iSandwich app.

## Deployment 
My website is currently up on Github Pages -  (the iSandwich project is using Flask, so view instead on Heroku, see link below.)

My webiste is currently up on Heroku - https://isandwich.herokuapp.com/

This project development has been done by using Gitpod, CI Gitpod Full Template and code repository is on GitHub. The produciton site has been deployed on Heroku.

Be sure that you have got Python, PIP and Git installed. If not do that before using/cloning this project.

### How to deploy this file on Heroku:

1. First navigate to Gitpod worskapce. 

2. Create a file: 'requirement.txt, including a list of dependencies needed for this project, by typing this terminal command:

pip3 freeze > requirements.txt

3. Create a file: 'Procfile' (Very important for Heroku in order to define the starting point), typ the command:

echo web: python run.py > Procfile

5. Push these files to the GitHub repository with the commands:

git add .'
git commit -m ”(Your message)”
git push

6. Open Heroku and create a new app with an unique app name (Heroku let you know if your name is available or not) and then choose your region.

7. Then login into Heroku in Gitpod workspace with the command Heroku login -i, the Heroku username and password are required here to be able to login.

8. Push the iSandwich project to Heroku with the type command:

git push heroku master

9. Go back to your app in Heroku in your browser, select the 'Settings'-tab, click on "Reveal Config Vars" and set the following config vars:

IP:  and 0.0.0.0
PORT: and 5000
MONGO_URI: and <link to your MongoDB database> (must be the same as in your file env.py)

10. Navigate back to Heroku and enable automatic deployment.

Connect Heroku to deploy from the master branch of DannyNagyAI-DannyNagyAI-Code-Institute-MS3-Project repository.

Successfully deploy the application.


## Deploying this site on heroku


1. Go to your browser and type Heroku.com and login.
2. Click to dashboard and click on the new app button.

3. Then select create new Heroku app.

4. Enter a new and unique app name (Heroku will let you know if the app name is available or not).

5. Select your region.

6. Set up the connection to the Github Repository:

7. First click the deploy button and then select GitHub - Connect to GitHub. 

8. A prompt to find a github repository to connect to will then be displayed. Enter the repository name for the project and click search. Once the repo has been found, click the connect button. Set environment variables:

Click the settings tab and then click the Reveal Confid Vars button and add the following:
key: IP, value: 0.0.0.0
key: PORT, value: 5000
key: MONGO_DBNAME, value: (your database name)
key: MONGO_URI, value: (mongo uri - This can be found on your mongoDB account)

9. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

## Credits

### Content 
All of the content on the website is an example/fictive.

### Mentors 
Got a lot of help from my mentor Oluwafemi Medale and again also some great coaching from my local mentor in Sweden, a Software developer named Daniel Sweder. He truly is an IT-genius!

### Media 
All of the photos used on this site were obtained from Shutterstock and Google. 

###### Acknowledgements and References
- [Code Institute](https://www.codeinstitute.net/) - I used what I learned so far from Code Instiute (FLASK/PYTHON/HEROKU/HTML/CSS/Boostrap). 
- [Flask](https://www.tutorialspoint.com/flask/flask_quick_guide.htm) - I used this webiste to learn more about flask and to get more inspiration.
- [Flask](https://stackoverflow.com/) - I also used this webiste to learn more about flask and to get more inspiration.
- [MongoDB](https://www.mongodb.com/cloud/atlasi) - I used this to learn more about MongoDb and to use the database. 
- [Bootstrap](https://startbootstrap.com/theme/clean-blog) - I used this template to be able to build my website.
- [Python](https://startbootstrap.com/theme/clean-blog) - I used this footer to able to shape the footer on all pages.

### by Daniel
