from zone import *
from items import *
class Player_Data:
    def __init__(self, location):
        self.name = None
        self.score = 0
        self.location = location
        self.inventory = []
        self.actions = {'Take': "Item added to your inventory!", 'drop': "you left the item behind!"}
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

    def score_return(self):
        return(self.score)
    # make it show current location

    def set_location(self):
        self.index += 1
        self.current_locale = self.location[self.index]

    def item_use_key(self):
        {'take':"You took the item!", 'use': "you used the item!",
         'drop': "You left the item behind!"}

    # make this one get the current location
    def loc_get(self):
        return(self.current_locale)

    # take item from itemlist in zone, add to inventory for player
    def take(self):
        item_list = self.current_locale.get_item_list()
        for i in item_list:
            self.inventory.append(i)
            print('{} was added to the inventory!'.format(i.get_name()))

    def inventory_show(self):
        for i in self.inventory:
            print(i.get_name())

    # use an item from inventory list
    def use_item(self, item):
        if item in self.inventory:
            return(item)

    # drop an item, removes it from list
    def drop_item(self):
        item_list = self.current_locale.get_item_list()
        for i in item_list:
            return "{} was dropped ".format(i.get_name())

    def get_actions_taken(self):
        return(self.actions_taken)

    def set_act_taken(self):
        self.actions_taken += 1

    # counts how many turns 
    def timer(self):
        print("You completed the game in:", self.actions_taken, "Turns.")
    

def main():
    locations = location_test(backpack,Wisp_in_bottle,coat,coin)
    # locations[2].get_item_list()
    player = Player_Data(locations)
    player.loc_get().describe()
    player.update_score()
    player.loc_get().choose_action(player)
    player.timer()
main()
