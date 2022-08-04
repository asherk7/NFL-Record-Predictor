from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

"""
To Do
create a seperate file to grab data from csv files and return it in the form of a list
then import the file here, when the user submits their prediction, use the function
to get the data(based on the team), then send it to database
then submit that data to the html file and use jinja to show it
edit the csv files and make each team name the exact same throughout all files
use jinja and send lists into main file containing teams from each division
check if a team is in a division(list), and add it to a seperate table of that specific division
"""

app = Flask(__name__) #references this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prediction.db' #creates database
db = SQLAlchemy(app) #initializes database with file

class Record(db.Model): #creating a database for user record prediction
    id = db.Column(db.Integer, primary_key=True)
    record = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self): #returns a string representation of the object
        return '<prediction %r>' % self.id

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(40), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<team %r>' % self.id

@app.route('/', methods=['POST', 'GET']) #gives the route options of receiving form data(post)
def index(): #creating main route
    if request.method == 'POST': #if the route is being sent data
        if request.form['redirect'] == 'ML':
            return redirect('/ml_info')

        else:
            team_data = Teams(team=request.form['teams'])
            record = request.form['predictions']
            if record.replace('-', '').isdigit():
                user_pred = Record(record=record)
            else:
                return 'Data was entered wrong' #make this a message on the website
            
            try:
                db.session.add(user_pred) #adding those instances to the database
                db.session.add(team_data)
                db.session.commit() #commiting the data to the session
                return redirect('/') #sending user back to the page
            except:
                return 'There was an error adding your prediction'

    else:
        team = Teams.query.order_by(Teams.date_created).all() #ordering the teams database in the date created
        prediction = Record.query.order_by(Record.date_created).all()
        #query goes through everything in database and gets those that are apart of that class
        return render_template('main.html', team_prediction=zip(team, prediction), team_length = team) #sending the data to the page to process and show

@app.route('/ml_info', methods=['POST', 'GET'])
def machinelearning():
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('ML_info.html')

@app.route('/delete/<int:id>') #routes to delete, and database's id
def delete(id):
    prediction_delete = Record.query.get_or_404(id) #grabbing the unique id
    team_delete = Teams.query.get_or_404(id)
    try:
        db.session.delete(prediction_delete)
        db.session.delete(team_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that prediction'

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)
