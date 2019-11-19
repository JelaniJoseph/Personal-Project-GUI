from classes import Item, Location

map_description = ""

class Map(Item):
    def __init__(self, current_location):
        Item.__init__(self, map_description)
        self.current_location = current_location

    def update_loc(self, new_location):
        if isinstance(new_location, Location):
            self.current_location = new_location

    def get_location(self):
        return self.current_location



        