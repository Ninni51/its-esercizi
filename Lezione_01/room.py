class Room:
    def __init__(self, id:str, floor:int, seats:int) -> None:
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats*2
    
    def get_floor(self, floor:str) -> int:
        return self.floor
    
    def get_id(self, id:str) -> str:
        return self.id
    
    def get_seats(self, seats:int) -> int:
        return self.id
    
    def get_area(self, area) -> int:
        return self.area

class Building:
    def __init__(self, name:str, address:str, floors:int, rooms:list) -> None:
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = rooms
    
    def get_floors(self, floors) -> list:
        return self.floors
    
    def get_rooms(self, rooms) -> list:
        return self.rooms
    
    def add_room(room):
        if room.floors in Building.floors:
    
    def get_area(self, area) -> int:
        totalarea = 0
        for area in Building.floors:
            totalarea += area
        return totalarea