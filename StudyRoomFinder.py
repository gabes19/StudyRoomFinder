from flask import Flask, render_template, request,redirect,url_for
from models import Library, RoomAvailabilitySnapshot, Room, RoomAvailabilityChange
from sqlalchemy import create_engine, func, extract
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import datetime, timedelta
from config import Config 
from zoneinfo import ZoneInfo
import humanize
import plotly.express as px

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

@app.route('/analytics')
def analytics():
    session = db_session
    #TODO: For the future, implement caching of most recent reservations to limit db queries
    #% of available slots reserved for the day, per room.
    def room_utilization_rate(session):
        #query all room availability changes for the day
        todays_snapshots = session.query.query()
        #cache recent total_reserved
        #aggregate td_reserved by total_reserved += len(td_reserved)
        #calculate by taking total_reserved/ total num of timeslots avaiable at the beginning of the day *100

        pass
    
    def hour_vs_day():
        pass

    def availability_vs_demand():
        pass

    def cumulative_reservations():
        pass

    def library_share():
        pass


    return render_template('analytics.html')

#TODO: Maybe make room times clickable? (in another function)
@app.route('/show_availability', methods=['POST'])
def show_availability():
    selected = request.form.get('location')
    if not selected:
        return redirect(url_for('index'))
    libraries = db_session.query(Library).order_by(Library.library_name).all()
    now_est = datetime.now(ZoneInfo("America/New_York"))
    timestamp = now_est.strftime('%A, %B %d, %Y — %I:%M %p')

    #fetch the library, its rooms, and recent snapshot
    lib = (db_session.query(Library).filter_by(library_name=selected).first())
    rooms = db_session.query(Room).filter_by(library_id=lib.id).all()
    availability_by_room = []
    for room in rooms:
        snapshot = (db_session.query(RoomAvailabilitySnapshot).filter_by(room_id = room.id)
              .order_by(RoomAvailabilitySnapshot.captured_at.desc())
              .first())
        if snapshot:
            captured_at_est = snapshot.captured_at.astimezone(ZoneInfo("America/New_York"))
            captured_time_diff = humanize.naturaltime(now_est - captured_at_est)
            times = snapshot.td_available_times if snapshot else []
            if times:
                availability_by_room.append({'room_name': room.room_name, 'times': times, "last_updated": captured_time_diff})

    return render_template('index.html',
                           libraries=libraries,
                           selected_location=selected,
                           availability_by_room=availability_by_room,
                           timestamp=timestamp)



#Session cleanup
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

