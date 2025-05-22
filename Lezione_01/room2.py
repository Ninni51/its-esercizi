class Room:
    def __init__(self, id: str, floor: int, seats: int) -> None:
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats*2 
    
    def get_floor(self) -> int:
        return self.floor
    
    def get_id(self) -> str:
        return self.id
    
    def get_seats(self) -> int:
        return self.seats
    
    def get_area(self) -> int:
        return self.area

class Building:
    def __init__(self, name: str, address: str, floors: int) -> None:
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []
    
    def get_floors(self) -> int:
        return self.floors
    
    def get_rooms(self) -> list:
        return self.rooms
    
    def add_room(self, room: Room) -> None:
        if 0 <= room.get_floor() <= self.floors:
            self.rooms.append(room)
        else:
            print("The room you were trying to add is not in the building.")

    def get_area(self) -> int:
        total_area = sum(room.get_area() for room in self.rooms)
        return total_area
    
building = Building(name="Test Building", address="123 Test St", floors=5)
print(type(building.floors))
