from django.contrib.auth.models import User
from adventure.models import Player, Room
import random

Room.objects.all().delete()

class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x

        # Start from center
        x = size_x//2
        y = size_y//2
        room_count = 0

        previous_room = None
        prev_dir = None

        adjectives = ["New", "Old", "Rocky", "Musty", "Dark", "Forbidding", "Cobwebbed", "Hidden", "Depressed", "Glorious"]
        nouns = ["Grotto", "Grove", "Pointe", "Place", "Venue", "Shire", "Plateau", "Passageway", "Hollow", "Dungeon"]

        location_info = []

        for adj in adjectives:
            for noun in nouns:
                location_info.append((adj, noun))

        random.shuffle(location_info)

        # While there are rooms to be created...
        while room_count < num_rooms:
            directions = []
            if x < size_x - 1 and prev_dir != 'w':
                directions.append('e')
            if x > 0 and prev_dir != 'e':
                directions.append('w')
            if y > 0 and prev_dir != 'n':
                directions.append('s')
            if y < size_y - 1 and prev_dir != 's':
                directions.append('n')

            room_direction = random.choice(directions)
            prev_dir = room_direction
            if room_direction == 'n':
                y += 1
            elif room_direction == 'e':
                x += 1
            elif room_direction == 's':
                y -= 1
            else:
                x -= 1

            # If room already exist, call it back
            if self.grid[y][x]:
                room = self.grid[y][x]
            # Create room only if room doesn't exist yet
            else:
                room = Room(title=f"The {location_info[room_count][0]} {location_info[room_count][1]}",
                            description=f"A Very {location_info[room_count][0]} {location_info[room_count][1]}", x=x, y=y)
                room.save()
                self.grid[y][x] = room
                room_count += 1
            # Note that in Django, you'll need to save the room after you create it

            reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}

            # Connect the room to the previous room
            if previous_room is not None:
                previous_room.connectRooms(room, room_direction)
                room.connectRooms(previous_room, reverse_dirs[room_direction])
                
            # Update iteration variables
            previous_room = room

        players=Player.objects.all()
        for p in players:
            p.currentRoom=room.id
            p.save()

w = World()
num_rooms = 100
width = 31
height = 11
w.generate_rooms(width, height, num_rooms)