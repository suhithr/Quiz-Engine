#!/usr/bin/python
from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager, login_user, login_required, logout_user

import json
from forms import LoginForm, RegisterForm

#Create the app and configure it
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

#Create Database object
db = SQLAlchemy(app)

#Create Bcrypt object
bcrypt = Bcrypt(app)

#Importing the models after creation of the app
from models import *

#Create instance of LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

#Configuring the login_manager object
login_manager.login_view = 'login'
login_manager.login_message = 'Please login to view this page'

@app.route('/')
@login_required
def home():
	return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST':
		print "first"
		if form.validate_on_submit():
			print "Second"
			user = User.query.filter_by(username=request.form['Username']).first()
			print
			if user is not None:
				login_user(user)
				flash('You have been logged in.')
				print "Success"
				return redirect(url_for('home'))
			else:
				error = 'Invalid Credentials, try again'
		else:
			error = 'Invalid Credentials, try again'
			render_template('login.html', form=form, error=error)
	return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(
			name=form.name.data,
			username=form.username.data,
			password=form.password.data
		)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect(url_for('home'))
	return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out')
	return redirect(url_for('login'))

#Starting the server with the run method
if __name__ == '__main__':
	app.run()