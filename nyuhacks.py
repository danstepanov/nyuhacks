from datetime import datetime

from flask import Flask, request, render_template, redirect, url_for
from flask.ext.mongokit import MongoKit, Document

app = Flask(__name__)

class Submit(Document):
	__collection__ = 'stories'
	structure = {
		'title': unicode,
		'story': unicode,
		'neighborhood': unicode,
	}
	required_fields = ['title','story','neighborhood']
	use_dot_notation = True

db = MongoKit(app)
db.register([Submit])

#@app.route('/new', methods=["GET", "POST"])
#def new_submit():
#	if request.method == 'POST':
#		submit = db.Submit()
#		submit.title = request.form['title']
#		submit.story = request.form['story']
#		submit.neighborhood = request.form['neighborhood']
#		submit.save()
#		return redirect(url_for('show_all'))
#	return render_template('index.html')

# Input stories
	# Title
	# Story
	# Location (lat and lng)
# Pull a collection of stories
	# Based on a certain distance around you
# Be able to flag a story
