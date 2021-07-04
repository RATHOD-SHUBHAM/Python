'''
if pip3 install flask gives an error try
sudo pip3 install flask

#command to create a requirement file
pip3 freeze > requirements.txt

#command to create a .py file
touch application.py

#run flask
run this everytime you open up terminal
export FLASK_APP=application.py
export FLASK_ENV=development
flask run

# install from requirements
pip3 install -r requirements.txt

'''

# creating flask application
from flask import Flask,request
app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy
#config database
# this will create a sqlite database called data.db in same directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


#connecting to database
class Drink(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),unique = True,nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return 'Hello--Welcome to home Page!!'

# get request = R
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    # we cant just display drinks
    # so we try to convert it into JSON type
    op = []

    for drink in drinks:
        drink_data = {'name':drink.name,'description':drink.description}
        op.append(drink_data)

    return {"drinks":op}


@app.route('/drinks/<id>')
def get_drink_by_id(id):
    drink = Drink.query.get_or_404(id)
    return {"name":drink.name, "description":drink.description}


# post = C
@app.route('/drinks',methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'],description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id} #check in postman


# delete = D
@app.route('/drinks/<id>',methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error":"404 Not FOUND"}
    db.session.delete(drink)
    db.session.commit()
    return {"message":"deleted"}