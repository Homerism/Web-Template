import datetime
from App.database import db

class Cart(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    
    def toDict(self):
      return{
        'cid':self.id,
        'text':self.text,
        'product_id':self.product_id
      }
    