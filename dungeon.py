#!/usr/bin/python
import random

NESW = ((0,-1), (1,0), (0,1), (-1,0))

class Room(object):
    def __init__(self, x,y):
        self.pos = (x,y)
        self.x, self.y = x, y
        self.dungeon = get_dungeon()
        self.no_connections = random.choice(self.get_roomtype_connections())

    def get_connections(self):
        return [self.dungeon.get_room_NESW(self.pos, pos) for pos in NESW]

    def get_roomtype_connections(self): return None
    def get_connection_type(self): return []
    def __str__(self): return ""

class EmptyRoom(Room):
    def get_roomtype_connections(self): return [0]
    def get_connection_types(self): return []
    def __str__(self): return " "
    
class Terminator(Room):
    def get_roomtype_connections(self): return [1]
    def get_connection_types(self): return [Corridor]
    def __str__(self): return "E"

class Corridor(Room):
    def get_roomtype_connections(self): return [3,4]
    def get_connection_types(self): return [Corridor]
    def __str__(self): return "C"

class Start(Room):
    def get_roomtype_connections(self): return [4]
    def get_connection_types(self): return [Corridor]
    def __str__(self): return "S"

class Boss(Terminator):
    def __str__(self): return "B"
class Shop(Terminator):
    def __str__(self): return "M"
class Treasure(Terminator):
    def __str__(self): return "T"
class Hidden(Terminator):
    def __str__(self): return "H"

class Dungeon(object):
    def __init__(self, size, num_rooms, floor):
        self.size = size
        self.num_rooms = random.choice(num_rooms)
        self.init_rooms = []
        self.max_retries = 50

    def __str__(self):
        string = "+"+"-"*self.size[0]+"+\n"
        for i_in, i in enumerate(self.pieces):
            string+= "|"
            for j in i:
                string+=str(j)
            string+="|\n"
        string+="+"+"-"*self.size[0]+"+\n"
        return string

    def init(self):
        done = False
        while not done:
            self.add_rooms()
            done = self.modify_rooms()
    
    def modify_rooms(self):
        terminator_types = [Boss, Shop, Treasure, Hidden]
        shuffled_rooms = range(len(self.init_rooms))
        random.shuffle(shuffled_rooms)
        for room_index in shuffled_rooms:
            room = self.init_rooms[room_index]
            if self.get_no_empty_rooms(room.get_connections()) == 3 and room.__class__ == Corridor:
                self.pieces[room.pos[0]][room.pos[1]] = Terminator(*room.pos)
                self.init_rooms[room_index] = self.pieces[room.pos[0]][room.pos[1]]
            if self.init_rooms[room_index].__class__ == Terminator and terminator_types != []:
                pos = self.init_rooms[room_index].pos
                new_type = terminator_types.pop()
                self.pieces[pos[0]][pos[1]] = new_type(*pos)
                self.init_rooms[room_index] = self.pieces[room.pos[0]][room.pos[1]]        
        return terminator_types == []

    def add_rooms(self):
        self.init_pieces()
        self.init_rooms = []
        i=0
        while len(self.init_rooms) != self.num_rooms:
            i+=1
            if self.add_room(i) == False:
                self.init_rooms = []
                self.init_pieces()
                i = 0
    
    def add_room(self, room_number):
        if room_number == 1:
            self.init_room(Start, (int(self.size[1]/2), int(self.size[0]/2)))
        else:
            chosen = False
            i = 0
            while not chosen:
                i+=1
                if i == self.max_retries:
                    return False
                room = random.choice(self.init_rooms)
                empty_list = map(self.room_empty, room.get_connections())
                if room.no_connections > 4-sum(empty_list):
                    room_type = random.choice(room.get_connection_types())
                    room_connections = self.true_indexes(empty_list)
                    room_pos = self.get_offset_NESW(room.pos, NESW[random.choice(room_connections)])
                    if self.get_no_empty_rooms(self.pieces[room_pos[0]][room_pos[1]].get_connections()) == 3:
                        self.init_room(room_type, room_pos)
                        chosen = True

    def init_room(self, room_type, pos):
        self.pieces[pos[0]][pos[1]] = room_type(*pos)
        self.init_rooms.append(self.pieces[pos[0]][pos[1]])

    def init_pieces(self):
        self.pieces = [[EmptyRoom(j, i) for i in range(self.size[0])] for j in range(self.size[1])]

    def get_room_NESW(self, pos, offset):
        total_pos = (pos[0]+offset[0], pos[1]+offset[1])
        if total_pos[0] >= 0 and total_pos[0] < self.size[1] and \
                total_pos[1] >= 0 and total_pos[1] < self.size[0]:
            return self.pieces[total_pos[0]][total_pos[1]]
        
    def get_offset_NESW(self, pos, offset):
        return (pos[0]+offset[0], pos[1]+offset[1])
        
    def true_indexes(self, bool_list):
        return [index for index, value in enumerate(bool_list) if value]

    def get_no_empty_rooms(self, room_list):
        return sum(map(self.room_empty, room_list))

    def room_empty(self, room):
        return room.__class__ == EmptyRoom

class Main(object):
    def __init__(self, floors):
        globals()["main"] = self
        self.floors = floors
        self.size = (9, 6)
        self.num_rooms = [(8,9), (11,12), (13,14), (16,17), (18,19)]
        self.num_rooms.extend([(20,) for i in range(floors-5)])
        self.dungeons = [Dungeon(self.size, self.num_rooms[i], i) for i in range(floors)]
        self.current_floor = -1
        for i in range(self.floors):
            self.next_floor()

    def get_current_dungeon(self):
        return self.current_dungeon

    def next_floor(self):
        self.current_floor+=1
        self.current_dungeon = self.dungeons[self.current_floor]
        self.current_dungeon.init()
        print(self.current_dungeon)

def get_main():
    return globals()["main"]

def get_dungeon():
    return get_main().get_current_dungeon()

if __name__ == "__main__":
    Main(6)
