from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #references this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prediction.db' #creates database
db = SQLAlchemy(app) #initializes database with file

class Todo(db.Model): #creating a database for user record prediction
    id = db.Column(db.Integer, primary_key=True)
    record = db.Column(db.String(200), nullable = False)

    def __repr__(self): #returns the record everytime a new element is made
        return '<prediction %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index(): #creating main route
    if request.method == 'POST':
        if request.form['redirect'] == 'predictions':
            return redirect('/records')
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
        if request.form['redirect'] == 'homepage':
            return redirect('/')
        else:
            user_content = request.form['prediction'] #id/name of the input
            user_prediction = Todo(record=user_content) #creating an object

            try:
                db.session.add(user_prediction) #adding user input to the database session
                db.session.commit()
                return redirect('/records') #redirecting back to the same page
            except:
                return 'There was an issue adding the prediction'

    else:
        predictions = Todo.query.order_by(Todo.record).all() #grabs all the past predictions
        return render_template('record.html', predictions=predictions) #sends past inputs into the page to use

@app.route('/delete/<int:id>') #routes to delete, and database's id
def delete(id):
    prediction_delete = Todo.query.get_or_404(id) #grabbing the unique id

    try:
        db.session.delete(prediction_delete)
        db.session.commit()
        return redirect('/records')
    except:
        return 'There was a problem deleting that prediction'

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)
