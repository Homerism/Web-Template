from flask import Blueprint, render_template, flash, redirect, request, jsonify
from App.models import Product, Cart
from App.database import db
from flask_login import login_required, current_user

from App.controllers import (
  product_search,
  cart_total
)


index_views = Blueprint('index_views', __name__, template_folder='../templates')


######################### Template Routes ##############################

@index_views.route('/')
def index():
  products = Product.query.all() #Query products in database for viewing 
  carts = Cart.query.all() #Query all products that has been added to cart
  return render_template('app.html', total=cart_total(),products=products,carts=carts) #returns products and cart products

@index_views.route('/search', methods=['POST'])
def search_product():
  queryresults = str(request.form["searchproduct"]) #requests search term
  results = product_search(queryresults) #Searches for product in database
  count=0
  #Checking the amount of items in results (Returns item not found if count = 0)
  for item in results:
    count+=1
  if queryresults is None or queryresults =="": 
    flash("Please enter a product")
    return redirect('/')
  if count == 0: 
    flash("Sorry No products was found.")
    return redirect('/')
  else:
    carts = Cart.query.all()
    return render_template('app.html', results=results, carts=carts, total=cart_total()) #returns the products added to cart and the results for the searched term

@index_views.route('/addProduct/<id>', methods=['GET'])
def add_product(id):
  check = Cart.query.filter_by(product_id=id).first() #filters cart products to see if there is that product already added to cart
  if check:
    check.quantity+=1 #If product was already added to cart its quantity is increased
    flash("Product was already added quantity increased")
    db.session.add(check)
    db.session.commit()
    return redirect('/')
  else:
    product = Product.query.get(id) #adds product to cart 
    cart = Cart(quantity=int(1), product_id=product.id)
    flash("Product was added to cart")
    db.session.add(cart)
    db.session.commit()
    return redirect('/')

@index_views.route('/editCart/<cid>', methods=['POST'])
def edit_Cart(cid):
  data = request.form.get("quantity") #request the desired the quantity information
  cart = Cart.query.filter_by(cid=cid).first() #filters for the particular product in cart
  if data is None: #if no data was added and submit was clicked
    flash('Please Enter quantity...')
    return redirect(url_for('index'))
  if data <="0": #if data is less that or equal to zero the particular product is removed from cart
    db.session.delete(cart)
    db.session.commit()
    flash('Item was removed from cart!')
    return redirect(url_for('index'))
  else:
    cart.quantity = data #if data is greater than 0 the product quantity is updated
    db.session.add(cart)
    db.session.commit()
    flash('Item Quanity Updated!')
  return redirect(url_for('index'))