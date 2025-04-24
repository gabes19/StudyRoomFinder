from flask import Flask, render_template, request,redirect,url_for
from models import Library, RoomAvailabilitySnapshot, Room
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import datetime, timedelta
from config import Config 

#App setup
app = Flask(__name__)
app.config.from_object(Config)

#SQLAlchemy setup
DATABASE_URL = app.config["SQL_ALCHEMY_DATABASE_URI"]
engine = create_engine(DATABASE_URL, echo=False)
SessionFactory = sessionmaker(bind=engine)
db_session = scoped_session(SessionFactory)

@app.route('/')
def index():
    libraries = db_session.query(Library).order_by(Library.library_name).all()
    return render_template('index.html', libraries=libraries, selected_location=None, available_times=None)


@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/show_availability', methods=['POST'])
def show_availability():
    pass



#Session cleanup
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

