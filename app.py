from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #references this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db' #creates database
db = SQLAlchemy(app) #initializes database with file

class Todo(db.Model):
    team = db.Column(db.String, primary_key=True) #creating database for team and record
    record = db.Column(db.String(200), nullable = False)

    def __repr__(self): #returns the team name everytime a new element is made
        return '<Team %r>' % self.team

@app.route('/') #creating the main route
def index():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
    #db.create_all()
