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


    # make this one get the current location
    def loc_get(self):
        return(self.current_locale)


    # take item from itemlist in zone, add to inventory for player
    def take(self):
        locale_items = self.current_locale.get_item_list()
        for item in locale_items:
            self.inventory.append(item)
            print('{} was added to the inventory!'.format(item.get_name()))


    # Shows whats in the inventory
    def inventory_show(self):
        for article in self.inventory:
            print(article.get_name())

    def test_inventory(self, user_input):
        for article in self.inventory:
            print(article.get_name())
            if user_input == article.getname():
                print(article.item_display())
                return(article.item_use())

    # allows player to specify which object to use, and subtracts 1 from the item use
    def inventory_use(self):
        inventory_action = input("select which item you would like to use: ").lower()
        self.test_inventory(inventory_action)



    # drop an item, removes it from list
    def drop_item(self):
        item_list = self.current_locale.get_item_list()
        for i in item_list:
            return "{} was dropped ".format(i.get_name())


    # adds one to the player counter 
    def set_act_taken(self):
        self.actions_taken += 1


    # counts how many turns 
    def timer(self):
        print("You completed the game in:", self.actions_taken, "Turns.")





