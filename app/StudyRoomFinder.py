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

#TODO: Rework this logc
@app.route('/show_availability', methods=['POST'])
def show_availability():
    selected = request.form.get('location')
    libraries = db_session.query(Library).order_by(Library.library_name).all()

    # if “Show All”, just render with empty list
    #TODO: Fix this
    if selected == "Show All":
        return render_template('index.html',
                               libraries=libraries,
                               selected_location=selected,
                               available_times=[])

    # otherwise fetch the library, its rooms, and recent snapshots
    lib = (db_session.query(Library)
            .filter_by(library_name=selected)
            .first())

    room_ids = [r.id for r in db_session.query(Room.id).filter_by(library_id=lib.id).all()]
    snapshots = []
    for id in room_ids:
        snap = (db_session.query(RoomAvailabilitySnapshot).filter_by(room_id = id)
              .order_by(RoomAvailabilitySnapshot.captured_at.desc())
              .first())
        snapshots.append(snap)


    # flatten today’s slots
    available = []
    for s in snapshots:
        available += s.td_available_times

    return render_template('index.html',
                           libraries=libraries,
                           selected_location=selected,
                           available_times=available)



#Session cleanup
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

