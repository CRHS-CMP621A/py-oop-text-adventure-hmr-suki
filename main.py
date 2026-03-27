# Add your program code here.
from room import Room
kitchen = Room('Kitchen')
kitchen.set_description('A dank and dirty room buzzing with files.')

dining_hall =Room('Dining Hall')
dining_hall.set_description('A fancy and luxury room with numerous cuisine placed on the long table.')

ball_room =Room('Ball room')
ball_room.set_description('A obsolute room where heavy dust covered the floor.')

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen,'north')
dining_hall.link_room(ball_room,'west')
ball_room.link_room(dining_hall,'east')

current_room = kitchen
while True:
    print('/n')
    current_room.get_details()
    command = input('>')
    current_room = current_room.move(command)