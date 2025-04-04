class Room:
    def __init__(self,name,library,capacity):
        self.name = name
        self.library = library #Library object room belongs to
        self.capacity = capacity #String capacity of room
        self.available_times = [] #List[String] of available time slots for the room
        self.description = ""