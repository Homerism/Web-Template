import datetime
from App.database import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    category = db.Column(db.String(500)) 
    price = db.Column(db.Float)
    image = db.Column(db.String(1000)) 
    about = db.Column(db.String(500))  
    carts = db.relationship('Cart', backref="product", lazy=True)  

    def toDict(self):
      return{
        'id':self.id,
        'name':self.title,
        'category':self.release_date,
        'price':self.poster_url,
        'image':self.studio,
        'about':self.gross,
        'carts':self.carts
      }
    