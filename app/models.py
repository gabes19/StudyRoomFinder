import sqlalchemy as sa
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship, sessionmaker, declarative_base
from typing import List
from datetime import datetime


Base = declarative_base()
class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_name: Mapped[str] = mapped_column(nullable=False)
    capacity: Mapped[str] = mapped_column(nullable=False)
    library_id: Mapped[int] = mapped_column(ForeignKey("libraries.id"), nullable=False)
    library: Mapped["Library"] = relationship(back_populates="rooms")


class RoomAvailabilitySnapshot(Base):
    __tablename__ = "room_availability_snapshots"

    snapshot_id: Mapped[int] = mapped_column(primary_key=True)
    #Datetime snapshot data was captured
    captured_at: Mapped[datetime] = mapped_column(nullable=False)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    library_id: Mapped[int] = mapped_column(ForeignKey("libraries.id"))
    #Available times for the day snapshot was captured
    td_available_times: Mapped[List[str]] = mapped_column(JSON,nullable=False)
    td_num_times: Mapped[int] = mapped_column(nullable=False)
    #Available times for the day after snapshot was captured (nd = next day)
    nd_available_times: Mapped[List[str]] = mapped_column(JSON,nullable=False)
    nd_num_times: Mapped[int] = mapped_column(nullable=False)


class Library(Base):
    __tablename__ = "libraries"

    id: Mapped[int] = mapped_column(primary_key=True)
    library_name: Mapped[str] = mapped_column(nullable=False)
    num_rooms: Mapped[int] = mapped_column(nullable=False)
    rooms: Mapped[List["Room"]] = relationship(back_populates="library")

class RoomAvailabilityChange(Base):
    __tablename__ = "room_availability_changes"

    id: Mapped[int] = mapped_column(primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(nullable=False)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    prev_snapshot_id: Mapped[int] = mapped_column(ForeignKey("room_availability_snapshots.snapshot_id"))
    current_snapshot_id: Mapped[int] = mapped_column(ForeignKey("room_availability_snapshots.snapshot_id"))
    td_diff: Mapped[int] = mapped_column(nullable=False)
    nd_diff: Mapped[int] = mapped_column(nullable=False)
    td_reserved: Mapped[List[str]] = mapped_column(JSON,nullable=False)
    td_released: Mapped[List[str]] = mapped_column(JSON,nullable=False)
    nd_reserved: Mapped[List[str]] = mapped_column(JSON,nullable=False)
    nd_released: Mapped[List[str]] = mapped_column(JSON,nullable=False)

class AggregateChanges(Base):
    __tablename__ = "aggregate_changes"

    id: Mapped[int] = mapped_column(primary_key=True)
    library_id: Mapped[int] = mapped_column(ForeignKey("libraries.id"))
    timestamp: Mapped[datetime] = mapped_column(nullable=False)
    agg_td_diff: Mapped[int] = mapped_column(nullable=False)
    agg_nd_diff: Mapped[int] = mapped_column(nullable=False)
    td_num_reserved: Mapped[int] = mapped_column(nullable=False)
    td_num_released: Mapped[int] = mapped_column(nullable=False)
    nd_num_reserved: Mapped[int] = mapped_column(nullable=False)
    nd_num_released: Mapped[int] = mapped_column(nullable=False)
