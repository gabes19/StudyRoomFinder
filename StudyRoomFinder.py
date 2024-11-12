from flask import Flask, render_template, request,redirect,url_for 
import modules as mod
app = Flask(__name__)

@app.route('/')
def index():
    selected_location = request.args.get('selected_location')
    return render_template('index.html', selected_location = selected_location)

@app.route('/about')
def about():
    return 'The About Page'


@app.route("/clark")
def clark():
    return render_template('clark.html')

@app.route('/show_availability', methods=['POST'])
def show_availability():
    location = request.form.get('location')
    return redirect(url_for('index', selected_location=location))

