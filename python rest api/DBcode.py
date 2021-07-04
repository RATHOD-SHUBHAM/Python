'''
write this code in terminal

or execute this file

'''

from application import db
from application import Drink
# create table
db.create_all()
drink = Drink(name="Coca-cola", description="Favourite Drink")
print(drink)

#add to table
db.session.add(drink)
db.session.commit()


#get all data
Drink.query.all()


'''
alternative inline command

db.session.add(Drink(name="Coca-cola", description="Favourite Drink"))query.all
'''