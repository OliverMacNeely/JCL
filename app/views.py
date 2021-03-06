from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():

	return render_template('index.html')
@app.route('/about-us')

def aboutUs():
	return render_template('about-us.html')

@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/blog-item')
def blogItem():
	return render_template('blog-item.html')

@app.route('/pricing')
def pricing():
	return render_template('pricing.html')

@app.route('/404')
def fourofour():
	return render_template('404.html')

@app.route('/blog-item-pub')
def blogpub():
	return render_template('blog-item-pub.html')

@app.route('/certamen')
def certamen():
	return render_template('certamen.html')

@app.route('/kickoff')
def kickoff():
	return render_template('kickoff.html')

@app.route('/states')
def states():
	return render_template('states.html')

@app.route('/nationals')
def nationals():
	return render_template('nationals.html')

@app.route('/midnight')
def midnight():
	return render_template('midnight.html')
