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

#TODO: Maybe make room times clickable? (in another function)
#TODO: Make sure you're only pulling up-to-date data for current rooms (rooms might be added, modified etc)
#ensure that snapshots are from the same batch

@app.route('/show_availability', methods=['POST'])
def show_availability():
    selected = request.form.get('location')
    if not selected:
        return redirect(url_for('index'))
    libraries = db_session.query(Library).order_by(Library.library_name).all()
    timestamp = datetime.now().strftime('%A, %B %d, %Y — %I:%M %p')

    #fetch the library, its rooms, and recent snapshot
    lib = (db_session.query(Library).filter_by(library_name=selected).first())
    rooms = db_session.query(Room).filter_by(library_id=lib.id).all()
    availability_by_room = []
    for room in rooms:
        snapshot = (db_session.query(RoomAvailabilitySnapshot).filter_by(room_id = room.id)
              .order_by(RoomAvailabilitySnapshot.captured_at.desc())
              .first())
        times = snapshot.td_available_times if snapshot else []
        if times:
            availability_by_room.append({'room_name': room.room_name, 'times': times})

    return render_template('index.html',
                           libraries=libraries,
                           selected_location=selected,
                           availability_by_room=availability_by_room,
                           timestamp=timestamp)



#Session cleanup
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

