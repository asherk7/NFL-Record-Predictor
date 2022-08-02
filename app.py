from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #references this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prediction.db' #creates database
db = SQLAlchemy(app) #initializes database with file

class Todo(db.Model): #creating a database for user record prediction
    record = db.Column(db.String(200), primary_key = True, nullable = False)

    def __repr__(self): #returns the record everytime a new element is made
        return '<Record %r>' % self.record

@app.route('/')
def index(): #creating main route
    return render_template('main.html')

@app.route('/records', methods=['POST', 'GET']) #methods allow us to send data to webpage
def records():
    if request.method == 'POST':
        user_content = request.form['content']
    else:
        pass

    return render_template('record.html')

if __name__ == '__main__':
    app.run(debug=True)
    #db.create_all()
