class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.linked_rooms = {}
        self.description= None

    def set_description(self,room_description):
        self.description=room_description
        self.linked_rooms = {}

    def get_description(self):
        return self.description
    
    def describe(self):
        print( self.description )

    def link_room(self,room_to_link,direction):
        self.linked_rooms[direction] = room_to_link
