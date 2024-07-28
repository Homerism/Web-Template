from App.models import Product, Cart 


#filters products based on search term provided
def product_search(search):
  return Product.query.filter(
    Product.name.like( '%'+search+'%' )
    | Product.about.like( '%'+search+'%' )
    | Product.category.like( '%'+search+'%' )
    )

#calculates the total of all cart items based on quantity and price
def cart_total():
  subtotal = 0
  cartitem = Cart.query.all()
  for item in cartitem:
    quantity = item.quantity
    price = item.product.price
    total = (quantity * price)
    subtotal += total
  subtotal = round(subtotal, 2)
  return subtotal