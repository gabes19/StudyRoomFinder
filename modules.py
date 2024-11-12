class StudyRoom:
    def __init__(self,name, library):
        self.name = name
        self.library = library
        available_times = [] #list of available time slots
        num_times = 0 #number of time slots
        capacity = ""

class Library:
    def __init__(self,name):
        self.name = name
        self.rooms = [] #list of StudyRooms
        self.num_rooms = 0 #number of StudyRooms

    def __str__(self):
        message = self.name + "Clark has the following availability:\n "
        for room in self.rooms:
            message += room.name + " Total Available Times: " + room.available_times + "\n"
        return message
    
def collect_clark():
    return

def collect_clem():
    return

def collect_rmc():
    return

def collect_shannon():
    return

def collect_music():
    return

def collect_finearts():
    return



