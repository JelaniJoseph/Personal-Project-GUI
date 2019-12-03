from zone import *
from items import *
class Player_Data:
    def __init__(self, location):
        self.name = None
        self.score = 0
        self.location = location
        self.inventory = []
        self.actions = {}
        self.actions_taken = 0
        self.index = 0
        self.current_locale = location[0]


   # sets playername to desired input
    def setname(self):
        print("Player Customization\n")
        print("=====================")
        self.name = input("Enter Username Here: ")
        print("The journey begins!")


    # gets username and allows it to be called later
    def getname(self):
        self.name
        return(self.name)


    # adds 5 to score everytime it's called
    def update_score(self):
        self.score += 5

    # make it show current location

    def set_location(self):
        self.index += 1
        self.current_locale = self.location[self.index]


    # make this one get the current location
    def loc_get(self):
        return(self.current_locale)

    # take item from locale, add in inventory
    def take(self, Location, item):
        # if item in #locale:
        self.inventory.append(item)  # remove item from locale

    # use an item from inventory list
    def use_item(self, item):
        if item in self.inventory:
            return(item)

    # drop an item, removes it from list
    def drop_item(self, inventory):
        inventory.remove(Items)

    def get_actions_taken(self):
        return(self.actions_taken)

    def set_act_taken(self):
        self.actions_taken += 1

    # counts how many turns 
    def timer(self):
        print("You completed the game in:", self.actions_taken, ".")
        return(self.actions_taken)
    

def main():
    locations = location_test(backpack,Wisp_in_bottle,coat,coin)
    player = Player_Data(locations)
    player.loc_get().describe()
    player.loc_get().choose_action(player)
main()
