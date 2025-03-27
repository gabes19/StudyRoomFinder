class Room:
    def __init__(self,name,library,capacity):
        self.name = name
        self.library = library
        self.capacity = capacity
        self.available_times = [] #List of available time slots for the room
        self.description = ""