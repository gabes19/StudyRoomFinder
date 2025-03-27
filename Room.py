import Library
class StudyRoom:
    def __init__(self,name, library):
        self.name = name
        self.library = library
        available_times = [] #List of available time slots for the room
        capacity = ""