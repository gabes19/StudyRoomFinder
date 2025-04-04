from flask import Flask, render_template, request,redirect,url_for 
app = Flask(__name__)

#TODO: FIX TEMPLATE SO SELECTED_LOCATION IS NOT NECESSARY CONTEXT
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
    location = request.form.get('location')
    available_times = None
    if location == "Clark Library":
        clark = mod.collect_clark()
        available_times =[{"name": room, "times": room.available_times} for room in clark.rooms]
    return redirect(url_for('index', selected_location=location, available_times = available_times))

