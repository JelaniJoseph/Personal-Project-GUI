from zone import *


from items import *


class Player_Data:
    def __init__(self, location):
        self.name = None
        self.score = 0
        self.location = location
        self.inventory = []
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
        return(self.name)


# adds 5 to score everytime it's called
    def update_score(self):
        self.score += 5


# returns the player score
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
    def take(self, lbl):
        locale_items = self.current_locale.get_item_list()
        for item in locale_items:
            self.inventory.append(item)
            lbl.config(text='{} was added to the inventory!'.format(item.getname()))
        return(item)


# shows whats in inventory, asks player to input item for use, if use is 0 then removes from inventory
    def inventory_show(self, lbl, inv_list):
        for article in self.inventory:
            inv_list.insert("end", article.getname())
        
    def inventory_use(self, lbl, inv_list):
        ans = False
        i = 0
        inventory_action = inv_list.get(inv_list.curselection())
        while((ans == False) and ( i < len(self.inventory)) ):
            if (inventory_action == self.inventory[i].getname()):
                ans = True
                lbl.configure(text= self.inventory[i].itemdisplay())
                self.inventory[i].item_use()
                if self.inventory[i].use == 0:
                    self.inventory.remove(self.inventory[i])
            else:
                 i+= 1


# drop an item, removes it from list
    def drop_item(self,lbl):
        item_list = self.current_locale.get_item_list()
        for i in item_list:
            lbl.config(text= "{} was dropped ".format(i.getname()))
        return(i)


# adds one to the player counter
    def set_act_taken(self):
        self.actions_taken += 1


# counts how many turns
    def timer(self):
        print("You completed the game in:", self.actions_taken, "Turns.")
