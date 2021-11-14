#QA DevOps Week 6 project 

This file is here to explain details on my app and how I developed it 

 

##Project brief: 

The brief for this project was to create a functioning web app which was CRUD functional, CRUD is defined as an app that has a user interface which one can Create, Read, Update and Delete the data. Beyond this the app had to include at least two databases with at least a one-to-many relationship.  

 

##My App: 

My app was modelled as a website for a company that provides temporary access to video games in return for a monthly subscription. Upon entering the application, the user is greeted to a homepage that presents the games currently available  

 

 

 The user can view the available games and can use a filter to see which games are available for each subscription. There are four buttons on the homepage: platinum, gold, silver and bronze. These buttons redirect the user to input customer information html page, from here they are given a selection of games to add to their account based on their chosen subscription tier and the subscription tier of the game, this game is then added to the customer’s profile. A ERD is shown below for the readers convenience in visualising this relationship.  

 

 ![ERD create customer](https://github.com/gbarnacle79/week_6_project/blob/main/Images/erd_createcustomer.png)

The ERD for the databases is shown below. 

![ERD database](https://github.com/gbarnacle79/week_6_project/blob/main/Images/erdp-database.png) 

After selecting a subscription tier and a game the customer would like to purchase the user’s data is added to the database and is automatically assigned an ID.

![createcustomer](https://github.com/gbarnacle79/week_6_project/blob/main/Images/Add_customer.png)

After submission the user is redirected to a webpage which shows data from the customer database. This information includes name, age, game ID and available options of either editing user data or cancelling subscription which deletes the customer from the database.  

![customer database page](https://github.com/gbarnacle79/week_6_project/blob/main/Images/customer_information_system.png) 

Clicking on the customer's name takes you to a new page that gives the details of the customer.At the top of the screen is a link that redirects the user back to the homepage.  

 ![homepage](https://github.com/gbarnacle79/week_6_project/blob/main/Images/homepage.png)

Clicking on a game’s name takes you to a new page that gives the details of the game. The game’s also have an operations section to and if one clicks on edit game they’re brought to a page where one can edit the details of the game to keep the records up to date. The “New Games!” links to a page which allows one to add a new game to the database and it is automatically assigned an ID 

 

###Continuous Integration: 

A Scrum board on JIRA was setup containing all the story points to create this app and the relevant issues to each story point, all these story points were put onto relevant epics and these were out into a sprint. 

  Once a task was complete the issue was marked as finished and if it turns out the original method set out in the issue was unfeasible then a comment was added to mention the change. This allowed for easy project tracking to allow me to check if I’m on track. 

 

The burndown chart is shown below 

![burndown chart](https://github.com/gbarnacle79/week_6_project/blob/main/Images/burndownchart.png) 

The version control system used was GitHub, this served as the repository for the project. The code was written out in Visual Studio Code which was linked to my git repository, the changes were committed and GitHub allows for viewing these commits and one can go back to a previous version of the code if there's any issues.  

The Visual Studio Code was linked to a virtual machine on the Google Cloud Platform and on this a python3 virtual environment was ran. The reason for the GCP VM was so that the code could be accessed even if my physical machine had an issue and the python3 virtual environment was used so that there would be no conflictions with installations and to follow best practice.  

 

The git repository was linked to a Jenkins server via a webhook. This Jenkins build server was created to allow for automated testing and building of the app. The Jenkins project had the secret key and the db_uri of the cloud SQL database, the build exports these and runs a build whenever a commit is sent to GitHub.  

 

###Tests: 

Tests were written in order to ensure each aspect of the application was running as intended, unit testing of the functions in the app was applied. The method used for unit testing was the pytest tool, specifically pytest-cover as this tool analyses the code and the tests written to produce a report to show which tests succeeded, which failed and what lines of the code have not been covered by the tests. A webhook was used to connect Jenkins to allow it to run a build on the new server and test it. Once a build is created and the tests are running the coverage report is saved as an artifact. 

![jenkins build](https://github.com/gbarnacle79/week_6_project/blob/main/Images/jenkins_build.png)

![coverage report](https://github.com/gbarnacle79/week_6_project/blob/main/Images/Coverage_report.png)

###Changes Made: 

In the initial outline of the project, it was intended for the details of the subscription tiers be held within a database. In practice this caused far more issues when it came to selecting a subscription tier and from this the games for that tier when entering the customers data. So instead, it was made into a field within both the customers and the games databases as this allowed a simple filter and a one-to-many relationship to be built between the two databases rather than between all three databases. This also reduced memory usage; however, it makes changing details for the subscription tiers more difficult.  

 

 

###Known Issues:  

When editing customer information, there is no filter on games. This allows customers to lower themselves to a cheaper subscription tier but still allow them to pick the higher tier games. In future builds this may be circumnavigated by when a customer edits there is a separate page where one first picks sub tier and then games, or not allow changing sub tier without deleting the account. 

 
