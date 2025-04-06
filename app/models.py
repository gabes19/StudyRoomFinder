# TODO: Edit/Create Models using SQLAlchemy
import sqlalchemy as sa
import app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
    declarative_base,
)
from datetime import datetime

database_url = app.config.SQL_ALCHEMY_DATABASE_URI
db = sa.create_engine(database_url)
Session = sessionmaker(bind=db)
Base = declarative_base()


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_name: Mapped[str] = mapped_column(nullable=False)
    capacity: Mapped[str] = mapped_column(nullable=False)
    library: Mapped["Library"] = relationship(back_populates="rooms")


class RoomAvailabilitySnapshot(Base):
    __tablename__ = "room_availability_snapshots"

    snapshot_id: Mapped[int] = mapped_column(primary_key=True)
    captured_at: Mapped[datetime] = mapped_column(nullable=False)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    available_times: Mapped[list[str]] = mapped_column(nullable=False)
    num_times: Mapped[int] = mapped_column(nullable=False)


class Library(Base):
    __tablename__ = "libraries"

    id: Mapped[int] = mapped_column(primary_key=True)
    library_name: Mapped[str] = mapped_column(nullable=False)
    num_rooms: Mapped[int] = mapped_column(nullable=False)
    rooms: Mapped[list["Room"]] = relationship(back_populates="library")
