from db import db
from app import app

db.init_app(app)

@app.before_first_request #run this before the first request before this app
def create_tables():
    db.create_all()  #only creates table it sees.