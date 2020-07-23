from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
#resource is a thing our api can return. usually mapped into database tables as well
#JWT jason web token. encoding data.
#once request sent and authentication met, we send the jwt to client who then sends jwt after each requests which shows
#that user has authenticated before.


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #when obj changed but no saved to db, this helps, but we turned it off.
app.secret_key = 'api'
api = Api(app) #help add resources to our app.


@app.before_first_request #run this before the first request before this app
def create_tables():
    db.create_all()  #only creates table it sees.


jwt = JWT(app, authenticate, identity) #/auth
#api works with resources and every resources have to be a class.



api.add_resource(Item, '/item/<string:name>') # need route to access that resource.
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList,'/stores')
if __name__ == '__main__':
    from db import db # we import cuz circular imports.
    db.init_app(app)
    app.run(port=5000, debug=True)