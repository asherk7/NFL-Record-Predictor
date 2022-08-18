# NFL Record Predictor: Project Overview 
#### Project Status: Active

* Created a tool that predicts each NFL team's record for the upcoming 2022-2023 season
* Scraped the data for each NFL team from multiple sources using Python and BeautifulSoup4
* Creating a website using HTML, CSS, Jinja, and Bootstrap to display the calculated predictions vs football analysts, and data
* Created a database with SQLAlchemy and SQlite to store user inputs
* Machine Learning model that will be used will use the Multiple Linear Regression model to use multiple impactful statistics to get the best outcome
* Building a website using Flask and deploying it using Heroku

## Code and Resources Used 
**Technologies:** python, html, css, bootstrap, api  
**Packages:** flask, sci-kit learn, sqlalchemy, beautifulsoup4, requests, csv, json  
**Flask:** https://www.youtube.com/watch?v=Z1RJmh_OqeA&ab_channel=freeCodeCamp.org  
**Machine Learning:** https://www.kaggle.com/learn/intro-to-machine-learning  
**Web Scraping:** https://www.youtube.com/watch?v=ng2o98k983k&ab_channel=CoreySchafer  
**HTML:** https://www.w3schools.com/html/  
**CSS:** https://www.w3schools.com/css/  

## Web Scraping
Used the web scraper above to scrape data for each NFL team, getting the following:
* Team name
* Average age
* Record Prediction
* Strength of Schedule
* Money spent on each position(QB, WR, RB, OL, CB, LB, S, DL)
* Money spent on offense and defense
* Offensive PPG
* Defensive points allowed
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
* Sorted each CSV file by team name in alphabetical order
* Changed the names of some teams so that it matched with all files

## Model Building
N/A (will use Multiple Linear Regression)

## Skills Learned
* I learned how to scrape data from websites using BeautifulSoup4
* I learned how to store the data scraped into CSV files
* I learned how to create a website using Flask
* I learned how to work with API's and JSON's
* I learned how to implement databases using SQLAlchemy
* I learned how to create a CRUD application
* I learned how to use Jinja and implement Bootstrap templates
* I became more knowledgeable with GIT
* Will learn how to deploy it using Heroku
* Will learn more advanced HTML and CSS
* Will learn how to create machine learning models using sci-kit learn

## Productionization
* The website is going to be deployed using Heroku

## Creator
* Created this project [myself](https://github.com/asherk7) using previous knowledge and tutorials of the basics, and built upon that foundation to complete the final product
* Inspiration: [CaPredictor](https://github.com/AliRZ-02/CaPredictor) by [Ali Raza Zaidi](https://github.com/AliRZ-02)
