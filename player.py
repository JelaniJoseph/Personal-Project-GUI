from zone import *
from items import *
class Player_Data:
    def __init__(self):
        self.name = None
        self.score = 0
        self.current_locale = None
        self.inventory = []
        self.actions = {}
        self.actions_taken = 0


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


# Lists available dictionary options for each zone
    # forest_options= {"left": "You take the left-most path", "right": "You take the right-side path","search": "You found a backpack!"}
    # forest_path_options = {"right": "You take the right path", "left": "You take the left path, but it seems to be a dead end!", "search": "You found a strange coin"}
    # cabin_options = {"search": "You found a coat, and a strange flask!", "rest": " You decide to rest a while...", "find an exit": "You look for a way out of the cabin"}
    # tundra_options = {"walk": "You try to push through the blizzard", "inventory": "you use the wisp in a bottle!", "map": "You open the map and see the pathway you must follow","backward": "it's too cold, you go back in the cabin"}
    # ocean_options = {"swim": "you swim downwards and reach an underwater cave"}
    # Tundra_Path_options = {"jump": "Afraid for your life you jump into the ocean", "fight": "you stand your ground!, but the monster claps you"}
    # cave_options = {"search": "you found a slot to insert some sort of coin", "continue": "you walk down the cave and soon find yourself in a series of tunnels"}
    # tunnel_options = {"map": "You pull out the map and see that you must make a right turn", "left": "You take the left-most path, but its a dead end...", "right": "you take the right-most path"}
    # house_options = {"wander": "you begin to look in all of the rooms",  "rest": "you decide to sit down and rest for a while"}
    # hospital_options =  {"waken": "You open your eyes and realize that you are now in a hospital"}

#gives a list of actions that are always available.
    # player_ready_actions = {'score': ("your score is", print(self.score)),
    #  'location': ("You are currently in", get_loc(Zone))), 'take': ("You took the", getname),
    #  'use': ("You used the ", use_item(item)), 'inventory': ("display items in inv")} # WIP

    # Lists available player actions
   
            
            
        # try: 
        #     for key, value in self.action_list.items():
        #         print("[]", key.capitalize())
        #         action = input("\nAction >> ").lower()
        #         self.actions_taken += 1
        #     if action in self.action_list:
        #         print(self.actions[action])
        #         return(True)
        # except KeyError:
        #     action = input("\n Incorrect, Try Again >>").lower()
        #     self.actions_taken += 1


    # make it show current location

    def get_loc(self, Zone):
        self.current_locale = Zone.name


    # make this one get the current location
    def locale_get(self, locations):
        print(self.current_locale)
        return(self.current_locale)

    # pick up an item and add it into inventory list
    def take_item(self, inventory):
        inventory.append() # remove specific, list inv user type in item to append

    # use an item from inventory list
    def use_item(self, item):
        if item in self.inventory:
            return(item)

    # drop an item, removes it from list
    def drop_item(self, inventory):
        inventory.remove()

    def get_actions_taken(self):
        return(self.actions_taken)

    def set_act_taken(self):
        self.actions_taken += 1

    # counts how many turns 
    def timer(self):
        print("You completed the game in:", self.actions_taken, ".")
        return(self.actions_taken)
    


def main():
    player = Player_Data()
    forest = Forest()
    forest.describe()
    forest.choose_action(player)
    player.timer()

main()
