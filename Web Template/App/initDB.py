import sys, os; sys.path.append(os.path.dirname(__file__) + '/..')
from App.models import Product, Cart
from App.database import db
import csv

# db.create_all(app=app)

def import_products_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for line in reader:
            product = Product(
                name=line['Product Name'],
                category=line['Category'] if line['Category'] else None,
                price=float(line['Selling Price']),
                image=line['Image'],
                about=line['About Product'] if line['About Product'] else None
            )
            db.session.add(product)
        db.session.commit()
        print('Database updated with products from CSV!')
