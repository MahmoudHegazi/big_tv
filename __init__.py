#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Menu, Series, Movie
from flask import session as login_session
import random
import string

# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
app = Flask(__name__)


engine = create_engine('sqlite:///bigtv.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



@app.route('/bigtv/<int:item_id>/series/<int:menu_id>/JSON')
def menuSeriesSON(item_id, menu_id):
    Menu_Item = session.query(Series).filter_by(id=menu_id).one()
    return jsonify(Menu_Item=Menu_Item.serialize)

@app.route('/bigtv/<int:item_id>/movies/<int:menu_id>/JSON')
def menuMoviesJSON(item_id, menu_id):
    Menu_Item = session.query(Movie).filter_by(id=menu_id).one()
    return jsonify(Menu_Item=Menu_Item.serialize)


@app.route('/bigtv/JSON')
def bigtvJSON():
    content = session.query(Menu).all()
    return jsonify(Content=[r.serialize for r in content])



# Show all series and movies
@app.route('/')
@app.route('/bigtv/', methods=['GET', 'POST'])
def showAll():
    movies = session.query(Movie).order_by(asc(Movie.name))
    series = session.query(Series).order_by(asc(Series.name))
    return render_template('index.html', movies=movies, series = series)
    

if __name__ == '__main__':
    app.secret_key = 'super_secret_key_forsideinrange(5):print(.##heLlowOrld!@#)'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
