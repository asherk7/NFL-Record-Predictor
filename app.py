from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from scripts.teamdata import team_stats, BRprediction, MLstats
from scripts import predictor

app = Flask(__name__) #references this file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prediction.db' #creates database
db = SQLAlchemy(app) #initializes database with file
divisions = [
            ['Buffalo Bills', 'New York Jets', 'Miami Dolphins', 'New England Patriots'],
            ['Cleveland Browns', 'Baltimore Ravens', 'Pittsburgh Steelers', 'Cincinnati Bengals'], 
            ['Houston Texans', 'Indianapolis Colts', 'Tennessee Titans', 'Jacksonville Jaguars'], 
            ['Las Vegas Raiders', 'Denver Broncos', 'Kansas City Chiefs', 'Los Angeles Chargers'], 
            ['New York Giants', 'Washington Commanders', 'Dallas Cowboys', 'Philadelphia Eagles'], 
            ['Chicago Bears', 'Detroit Lions', 'Minnesota Vikings', 'Green Bay Packers'], 
            ['Carolina Panthers', 'Atlanta Falcons', 'New Orleans Saints', 'Tampa Bay Buccaneers'], 
            ['San Francisco 49ers', 'Arizona Cardinals', 'Los Angeles Rams', 'Seattle Seahawks'], 
            ]

class Record(db.Model): #database for user record prediction
    id = db.Column(db.Integer, primary_key=True)
    record = db.Column(db.String(200), nullable = False)
    ML_record = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self): #returns a string representation of the object
        return '<prediction %r>' % self.id

class Teams(db.Model): #database for team and teamstats
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(40), nullable = False)
    teamstats = db.Column(db.String(100), nullable = False)
    BRprediction = db.Column(db.String(20))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<team %r>' % self.id

def error(message):
    team = Teams.query.order_by(Teams.date_created).all()
    prediction = Record.query.order_by(Record.date_created).all()
    team_statistics = Teams.query.order_by(Teams.date_created).all()
    error_message = f'There was an error {message} the prediction. The data may have been entered in the wrong format, or it may be a duplicate entry'
    return render_template('main.html', team_prediction=list(zip(team, prediction)), team_length = team, error=error_message, divisions=divisions, team_statistics=team_statistics)

@app.route('/', methods=['POST', 'GET']) #gives the route options of receiving form data(post)
def index(): #creating main route
    if request.method == 'POST': #if the route is being sent data
        team_data = Teams(team=request.form['teams'], teamstats=', '.join(team_stats(request.form['teams'])), BRprediction=BRprediction(request.form['teams']))
        #can't send a list into a database, so turned it into a string and will turn it back into a list in the html code with jinja
        for teamname in Teams.query.order_by(Teams.date_created).all():
            if team_data.team == teamname.team:
                return error('adding') #preventing duplicates

        ML_stats = MLstats(request.form['teams'])
        ML_pred = predictor.Predictor(ML_stats[0], ML_stats[1], ML_stats[2], ML_stats[3], ML_stats[4], 
                                        ML_stats[5], ML_stats[6], ML_stats[7], ML_stats[8], ML_stats[9])
        ML_record = ML_pred.get_prediction()

        wins = request.form['wins']
        losses = request.form['losses']
        ties = request.form['ties']
        if (int(wins) + int(losses) + int(ties)) != 17:
            return error('adding')
        else:
            record = f'{wins}-{losses}-{ties}'
            user_pred = Record(record=record, ML_record = ML_record)

        try:
            db.session.add(user_pred)
            db.session.add(team_data)
            db.session.commit() #commiting the data to the session
            return redirect('/')
        except:
            return error('adding')

    else:
        team = Teams.query.order_by(Teams.date_created).all() #ordering the teams database in the date created
        prediction = Record.query.order_by(Record.date_created).all()
        team_statistics = Teams.query.order_by(Teams.date_created).all()
        #query goes through everything in database and gets those that are apart of that class
        return render_template('main.html', team_prediction=list(zip(team, prediction)), team_length = team, divisions=divisions, team_statistics=team_statistics) #sending the data to the page to process and show
        #variable has to be sent in as a list in order to loop over it more than once, since an iterator can only loop once

@app.route('/user_prediction', methods=['POST', 'GET'])
def user_pred():
    if request.method == 'POST':
        team = request.form['teams']
        offppg = request.form['offppg']
        defppg = request.form['defppg']
        passtd = request.form['passtd']
        passyrd = request.form['passyrd']
        rushyrd = request.form['rushyrd']
        ypc = request.form['ypc']
        rushtd = request.form['rushtd']
        interception = request.form['int']
        fumble = request.form['fumble']
        user_pred = predictor.Predictor(team, defppg, offppg, passtd, passyrd, 
                                        rushyrd, ypc, rushtd, interception, fumble)
        record = user_pred.get_prediction()
        return render_template('user_pred.html', record=record, user_pred=user_pred)
    else:
        return render_template('user_pred.html')

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
        return error('deleting')

if __name__ == '__main__':
    db.drop_all() #resets the database
    db.create_all()
    app.run(debug=False, host='0.0.0.0', port=5000)
