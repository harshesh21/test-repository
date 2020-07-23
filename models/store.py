
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy='dynamic') #not go in items table and create a obj for each item by using lazy.
#by using lazy, items become query builder and so now in json method we need to call items.ALL() to retrieve all items.
    #lazy makes it slower because each time u call json , it goes thru items table.
    def __init__(self,name):
        self.name=name


    def json(self ):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]}#.all()

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() #query is basically Select * from items where name=name


    def save_to_db(self): #update and insert.
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()