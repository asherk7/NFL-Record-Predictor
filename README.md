# NFL Record Predictor: Project Overview 
#### Project Status: Active

* Created a tool that predicts each NFL team's record for the upcoming 2022-2023 season
* Scraped the data for each NFL team from multiple sources using Python and BeautifulSoup4
* Created a website using HTML, CSS, Jinja2, and Bootstrap4 to display the calculated predictions vs football analysts, and data
* Created a database with SQLAlchemy and SQlite to store user inputs
* Used the Decision Tree Regression Machine Learning model to predict each team's record
* Built a full-stack website using Flask and deployed it using Heroku

## Code and Resources Used 
**Technologies:** python, html, css, bootstrap4, api  
**Packages:** flask, sklearn, pandas, sqlalchemy, beautifulsoup4, requests, csv, json  
**Flask:** https://www.youtube.com/watch?v=Z1RJmh_OqeA&ab_channel=freeCodeCamp.org  
**Machine Learning:** https://www.kaggle.com/learn/intro-to-machine-learning  
**Web Scraping:** https://www.youtube.com/watch?v=ng2o98k983k&ab_channel=CoreySchafer  
**HTML:** https://www.w3schools.com/html/  
**CSS:** https://www.w3schools.com/css/  

## Web Scraping
Used the web scraper above to scrape data for each NFL team, getting the following:
* Team name
* Average age
* Record Prediction by Bleacher Report
* Strength of Schedule
* Money spent on each position(QB, WR, RB, OL, CB, LB, S, DL)
* Money spent on offense and defense
* Offensive PPG
* Defensive Points Allowed
* Team Completion Percentage
* Yards per Passing Attempt
* Yards per Reception
* Yards per Rush
* Quarterback Rating
* Receiving Yards and Touchdowns
* Rushing Yards and Touchdowns
* Team Win Percentage(2021)
* Interceptions, Sacks, Sack Yards, Fumbles

## Data Cleaning
After scraping the data, I cleaned it so it would be easily usable for the model. The following changes were made:
* Changed the names of some teams so that it matched with all files
* Sorted each CSV file by team name in alphabetical order
* Removed commas from numbers

## Model Building
First, I split the data into training and validation sets using train_test_split to see if the model was accurate with the data provided.

I then used the Multiple Linear Regression and Decision Tree Regression model and evaluated them using Mean Absolute Error to find which model was the most accurate.

The Decision Tree Regression model had an MAE(Mean Absolute Error) around 8%, while the Multiple Linear Regression model had an MAE around 15%, which lead me to using the Decision Tree Regression model since it had more than half the error rate.

## Skills Learned
* I learned how to scrape data from websites using BeautifulSoup4
* I learned how to store scraped data into CSV files
* I learned how to create a CRUD application using Flask
* I learned how to work with API's and JSON's
* I learned how to implement and work with databases using SQLAlchemy
* I learned how to work with and connect a front-end and back-end
* I learned how to use Jinja2 and implement Bootstrap4 templates
* I learned how to deploy a website using Heroku
* I learned how to create machine learning models using Sci-kit Learn
* I became more familiar with HTML and CSS
* I became more familiar with the pandas package
* I became more knowledgeable with GIT

## Productionization
* The website is being deployed using Heroku

## Creator
* Created this project [myself](https://github.com/asherk7) using previous knowledge and tutorials of the basics, and built upon that foundation to complete the final product
* Inspiration: [CaPredictor](https://github.com/AliRZ-02/CaPredictor) by [Ali Raza Zaidi](https://github.com/AliRZ-02)
