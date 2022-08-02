from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #references this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prediction.db' #creates database
db = SQLAlchemy(app) #initializes database with file

class Todo(db.Model): #creating a database for user record prediction
    record = db.Column(db.String(200), primary_key = True, nullable = False)
    team = db.Column(db.String(30))

    def __repr__(self): #returns the record everytime a new element is made
        return '<Record %r>' % self.record

@app.route('/', methods=['POST', 'GET'])
def index(): #creating main route
    if request.method == 'POST':
        return redirect('/records/')

    else:
        return render_template('main.html')

@app.route('/records/', methods=['POST', 'GET']) #methods allow us to send data to webpage
def records():
    if request.method == 'POST': #if the user is posting something
        user_content = request.form['prediction'] #id/name of the input
        user_prediction = Todo(record=user_content) #creating an object

        try:
            db.session.add(user_prediction) #adding user input to the database session
            db.session.commit()
            return redirect('/records/') #redirecting back to the same page
        except:
            return 'There was an issue adding the prediction'

    else:
        predictions = Todo.query.all() #grabs all the past predictions
        return render_template('record.html', predictions=predictions) #sends past inputs into the page to use

if __name__ == '__main__':
    app.run(debug=True)
    #db.create_all()
