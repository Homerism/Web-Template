from App.models import Product, Cart
from App.database import db
import csv
from App import create_app

app = create_app()

with open('products.csv', newline='') as csvfile:
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

print('database initialized!')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
