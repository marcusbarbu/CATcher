from flask import Flask, request, render_template, redirect
import requests
import random

CONTROLLER_URL = 'http://10.33.32.105:5000'
app = Flask(__name__)

global_awards_list = []
with open('awards', 'r') as awards:
	raw = awards.read()
	global_awards_list = raw.split('\n')

def load_badges():
	x = []
	for i in range(100):
		x.append({'award_category':random.choice(range(3)), 'award_text':random.choice(global_awards_list)})
	return x

def load_conversations():
	return 'adsf'

def load_cages():
	x = []
	for i in range(100):
		x.append({'status':random.choice(range(2)), 'id':i})
	return x

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cages')
def cage_list():
	return render_template('cages.html', cages = load_cages())

@app.route('/cage/<cageid>')
def single_cage_view(cageid):
	return render_template('singlecage.html', cage = {'id':cageid}, url = CONTROLLER_URL)

@app.route('/social')
def social():
	conversations = load_conversations()
	return render_template('social.html', threads = conversations)

@app.route('/badges')
def badges():
	user_badges = load_badges()	
	return render_template('badges.html', badges = user_badges)

@app.route('/cage/<cageid>/close')
def close_cage(cageid):
	print "closing cage " + cageid
	return redirect('/cage/' + cageid)

@app.route('/cage/<cageid>/open')
def open_cage(cageid):
	print "opening cage " + cageid
	return redirect('/cage/' + cageid)

@app.route('/cage/<cageid>/closeflap')
def close_flap(cageid):
	print "closing flap " + cageid
	return redirect('/cage/' + cageid)

@app.route('/cage/<cageid>/openflap')
def open_flap(cageid):
	print "opening flap " + cageid
	return redirect('/cage/' + cageid)

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')

