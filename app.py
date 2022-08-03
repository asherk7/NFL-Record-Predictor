from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) #references this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prediction.db' #creates database
db = SQLAlchemy(app) #initializes database with file

class Record(db.Model): #creating a database for user record prediction
    id = db.Column(db.Integer, primary_key=True)
    record = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self): #returns the record everytime a new element is made
        return '<prediction %r>' % self.id

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(40), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<team %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index(): #creating main route
    if request.method == 'POST':
        if request.form['redirect'] == 'predictions':
            team = request.form['teams'] #grabbing the team they selected
            return redirect(url_for('records', team=team)) #use url_for if sending info from one route to another
        else:
            return redirect('/ml_info')

    else:
        return render_template('main.html')

@app.route('/ml_info', methods=['POST', 'GET'])
def machinelearning():
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('ML_info.html')

@app.route('/records', methods=['POST', 'GET']) #methods allow us to send data to webpage
def records():
    if request.method == 'POST': #if the user is posting something
        if request.form['redirect'] == 'homepage': #used for multiple forms with name redirect
            return redirect('/')
        else:
            user_content = request.form['prediction'] #id/name of the input
            user_prediction = Record(record=user_content) #creating an object

            try:
                db.session.add(user_prediction) #adding user input to the database session
                db.session.commit()
                return redirect('/records') #redirecting back to the same page
            except:
                return 'There was an issue adding the prediction'

    else:
        try:
            user_team = request.args['team'] #grabs info sent from other route
            team_db = Teams(team=user_team)
            db.session.add(team_db)
            db.session.commit()
        except:
            pass
        predictions = Record.query.order_by(Record.date_created).all() #grabs all the past predictions
        teams = Teams.query.order_by(Teams.date_created).all()
        return render_template('record.html', team_prediction=zip(teams, predictions)) #sends past inputs into the page to use

@app.route('/delete/<int:id>') #routes to delete, and database's id
def delete(id):
    prediction_delete = Record.query.get_or_404(id) #grabbing the unique id
    team_delete = Teams.query.get_or_404(id)

    try:
        db.session.delete(prediction_delete)
        db.session.delete(team_delete)
        #del Record.query.get_or_404(id)
        #hide bar when user enters prediction, only show when redirected again(like deleting)
        #only delete record from database, so when they delete and enter again, it shows the same team
        #do something about going between teams first then entering predictions
        #also make it so their predictions are in a '#-#' format
        db.session.commit()
        return redirect('/records')
    except:
        return 'There was a problem deleting that prediction'

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)
