
# location_info = ['forest', 'Cabin', 'Tundra', 'Ocean', 'Cave', 'Tunnel', 'House', 'Hospital']
def get_int(user, result, limit):
    choice =input(user)  # gets the user input and compares it to paramaters
    while choice not in result:
        choice = input("Invalid command, try again: ")

class Player_Data:
    
    def __init__(self, current_locale, move_count):
        self.name = None
        self.score = 0
        self.current_locale = current_locale
        self.inventory = []
        self.move_count = move_count

   # sets playername to desired input
    def setname(self):
        print("Player Customization\n")
        print("=====================")
        self.name = input("Enter Username Here: ")
        print("The journey begins!")
    def getname(self):
        self.name
        return(self.name)
    # adds 5 to score everytime it's called
    def update_score(self):
        self.score += 5


# Displays current location for player according to list

def current_location(self, next_location):
    self.current_locale = next_location


# pick up an item and add it into inventory list
def take_item(self, inventory):
    inventory.append()

# use an item from inventory list
def use_item(self, item):
    if item in self.inventory:
        return(item)

# drop an item, removes it from list
def drop_item(self, inventory):
    inventory.remove()


# supposed to count player input and once it reaches set limit exits game
def timer(move_count, choice):
    self.move_count += 1
    if move_count >= 10:
        print("You took too long")
        print("The beast catches up and kills you")
        print("You Died...")
        quit()
    return(choice)


