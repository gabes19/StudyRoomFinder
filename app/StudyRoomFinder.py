from flask import Flask, render_template, request,redirect,url_for
from config import Config 

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    selected_location = request.args.get('selected_location')
    available_times = request.args.get('available_times')
    return render_template('index.html', selected_location = selected_location, available_times = available_times)

@app.route('/about')
def about():
    return render_template('about.html')
#TODO: Reimplement all the logic
@app.route('/show_availability', methods=['POST'])
def show_availability():
    pass

