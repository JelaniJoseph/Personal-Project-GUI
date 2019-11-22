
class Player_Data:

    def __init__(self, current_locale, actions):
        self.name = None
        self.score = 0
        self.current_locale = current_locale
        self.inventory = []
        self.actions = actions

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
    # Displays current location for player according to list
    def next_loc(self, locations):
        self.current_locale = locations[+1]

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

    # counts how many turns 
    def timer(self, actions, actions_taken):
        actions = input("What will you do?: ").lower()
        self.actions_taken += 1
        return(actions)

    def counter_return(self, actions_taken):
        print("You finished the game in:", actions_taken, "Turns!")


