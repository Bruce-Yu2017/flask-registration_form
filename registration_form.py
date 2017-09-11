from flask import Flask, render_template, request, redirect, session, flash, url_for
import re
import datetime
app = Flask(__name__)
app.secret_key = 'codingdojo'

@app.route('/')
def landing():
	return render_template('registration_form.html')

@app.route('/regiform', methods = ['GET', 'POST'])
def regi():
	EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
	count = 0
	session['email'] = request.form['email']
	session['firstname'] = request.form['firstname']
	session['lastname'] = request.form['lastname']
	session['password'] = request.form['password']
	session['confirm'] = request.form['confirm']

	if not EMAIL_REGEX.match(session['email']):
		flash('Invalid email address', 'error')
	elif len(session['email']) < 1:
		flash('Email can not be blank', 'error')
	else:
		count += 1

	if len(session['firstname']) < 1:
		flash('Please put in your first name.', 'error')
	else:
		count += 1

	if len(session['lastname']) < 1:
		flash('Please put in your last name.', 'error')
	else:
		count += 1

	uppercount = 0
	digitcount = 0
	for letter in session['password']:
		if letter.isupper():
			uppercount += 1

	for num in session['password']:
		if num.isdigit():
			digitcount += 1

	if uppercount == 0:
		flash('At least one uppercase letter in your password.', 'error')
	else:
		count += 1

	if digitcount == 0:
		flash('At least one number in your password.', 'error')
	else:
		count += 1

	if len(session['password']) < 1:
		flash('Please put in your password.', 'error')
	else:
		count += 1

	if len(session['confirm']) < 1:
		flash('Please confirm your password.', 'error')
	else:
		count += 1

	if session['password'] != session['confirm']:
		flash('Unpaired. Please confirm your password again.', 'error')
	else:
		count += 1

	if count == 8:
		flash("Thanks for submitting your information.")
		return redirect('/')
	else:
		flash("You still have some mistakes.", 'error')
		return redirect('/')





app.run(debug = True)