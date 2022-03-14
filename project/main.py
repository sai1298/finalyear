
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app=Flask(__name__)

@app.route('/')
def homepage():
	return render_template('homepage.html')

@app.route('/adminpage')
def adminpage():
	return render_template('adminpage.html')

if __name__ == '__main__':
	app.run(debug=True)
