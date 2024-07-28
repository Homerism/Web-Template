from flask import Blueprint, render_template, flash, redirect, request, jsonify, url_for
from App.database import db

index_views = Blueprint('index_views', __name__, template_folder='../templates')


######################### Template Routes ##############################

@index_views.route('/')
def index():
  return render_template('app.html')