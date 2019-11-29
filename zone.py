from items import *
backpack = Backpack()
coin = Coin()
coat = Coat()
bottle = Wisp_in_bottle()
class Zone:
    def __init__(self, name, description, actions, after, consequence, visited):
        self.name = name
        self.description = description
        self.actions = actions
        self.after = after
        self.consequence = consequence
        self.visited = False
        self.searched = False


    def describe(self):
        print(self.name)
        print("=========")
        print(self.description)


    def choose_action(self):
        for key, value in self.actions.items():
            print("[]", key.capitalize())
        action = input("\nAction >> ").lower()
        if action in self.actions:
            print(self.actions[action][0])
            return(True)
        else:
            action = input("\n Incorrect, Try Again >>").lower()
            self.choose_action()


    def area_visited(self):
        if self.visited == True:
            print("Playername has visited: ", self.name)


    def after_desc(self):
        print(self.after)


    def situational(self, action):
        print(self.actions[action])
        print(self.consequence)
        print("You Died...\n")
        quit()


class Forest(Zone):
    def __init__(self):
        Zone.__init__(self, "Forest", "You enter the Ominous Woods, there seems to be two paths",
        {"left": "You take the left-most path", "right": "You take the right-side path", "search":
         ("You found a backpack!", backpack)},
        "as you continue you hear a sinister roar, it seems your choices will now have consequences.\n",
        "text is within here", True)


class Forest_Path(Zone):
    def __init__(self):
        Zone.__init__(self, "Forest Pathway", "As you continue through the Forest you see a glint in the trees, and two pathways.", 
        {"right": "You take the right path","left": "You take the left path, but it seems to be a dead end!",
         "search": ("You found something", coin, True)}, 
         "You continue on!\n", "A pitch black humanoid creature with a smile appears, and kills you", True )


    def situational_actions(self, Forest_Path):
        try:
            for key, value in self.actions.items():
                print("[]", key.capitalize())
            action = input("\nAction >> ").lower()
            if action in self.actions and action != action in self.actions['left']:
                print(self.actions[action])
                Forest_Path.after_desc(self)
            elif action == action in self.actions['left']:
                Forest_Path.situational(self, action)
        except KeyError:
            action = input("\n Incorrect, Try Again >>").lower()
            self.situational_actions(Forest_Path)


class Cabin(Zone):
    def __init__(self):
        Zone.__init__(self, "Cabin", "You squint and can barely make out the figure of a log cabin",
        {"search": ("You found a coat, and a strange flask!", coat, bottle, True), "rest": " You decide to rest a while...",
        "find an exit": "You look for a way out of the cabin"}, "You prepare yourself, and push forward!\n",
        "text", True)


class Tundra(Zone): # add situational, if inventory  then skip to end
    def __init__(self):
        Zone.__init__(self, "Tundra", "The cold chips away at your very being",
         {"walk": "You try to push through the blizzard", "inventory": ("you use the wisp in a bottle!", bottle),
         "map": "You open the map and see the pathway you must follow","backward": "it's too cold, you go back in the cabin",},
         "After some time you reach an icy lake\n", "text", True)


class Tundra_Path(Zone):
    def __init__(self):
        Zone.__init__(self, "Tundra", "as you stare ath the ocean, you hear something dangerous approaching you",
        {"jump": "Afraid for your life you jump into the ocean",
         "fight": "you stand your ground!, but the monster claps you"}, "You sink into the icy depths of the water",
         "you lay there bleeding out, and cold.", True)


    def situational_actions(self, Tundra_Path):
        try:
            for key, value in self.actions.items():
                print("[]", key.capitalize())
            action = input("\nAction >> ").lower()
            if action in self.actions and action != action in self.actions['fight']:
                print(self.actions[action])
                Tundra_Path.after_desc(self)
            elif action == action in self.actions['fight']:
                Tundra_Path.situational(self, action)
        except KeyError:
            action = input("\n Incorrect, Try Again >>").lower()
            self.situational_actions(Tundra_Path)


class Ocean(Zone):
    def __init__(self):
        Zone.__init__(self, "Ocean", "you're underwater", {"swim": "you swim downwards and reach an underwater cave"},
        "As you enter the cave, the entrance behind you closes and the water dissapears", "text", True)


class Cave(Zone): # if player has coin here then loose
    def __init__(self):
        Zone.__init__(self, "Cave", "the area somehow feels alive...", {"search": 
        ("you found a slot to insert some sort of coin", coin, True),
         "continue": "you walk down the cave and soon find yourself in a series of tunnels"}, 
         "it's almost as if the area is shifting all on its own...", "text", True)


class Tunnel(Zone):
    def __init__(self):
        Zone.__init__(self, "Tunnel", "it's dark and you can sense something folowing you", 
        {"map": "You pull out the map and see that you must make a right turn",
        "left": "You take the left-most path, but its a dead end...", "right": "you take the right-most path"},
        "Soon you see a bright light and as you go towards it your area begins to change.",
        "You feel the tunnel begin to move and soon you are enveloped by the floor", True )


    def situational_actions(self, Tunnel):
        try:
            for key, value in self.actions.items():
                print("[]", key.capitalize())
            action = input("\nAction >> ").lower()
            if action in self.actions and action != action in self.actions['left']:
                print(self.actions[action])
                Tunnel.after_desc(self)
            elif action == action in self.actions['left']:
                Tunnel.situational(self, action)
        except KeyError:
            action = input("\n Incorrect, Try Again >>").lower()
            self.situational_actions(Tunnel)


class House(Zone): # check inventory to see if player has key, if so then print text and end
    def __init__(self):
        Zone.__init__(self, "House", "Feels safe and cozy...", {"wander": "you begin to look in all of the rooms",
        "rest": "you decide to sit down and rest for a while"}, "Suddenly, something feels strange...",
         "text", True )


class Hospital(Zone):
    def __init__(self):
        Zone.__init__(self, "Hospital", "strangely feels more real than what just happened...",
        {"waken": "You open your eyes and realize that you are now in a hospital"}, "Everything is finally over",
         "text", True )


def main():
    forest = Forest()
    forest.describe()
    forest.choose_action()
    forest.after_desc()
    forest2 = Forest_Path()
    forest2.describe()
    forest2.situational_actions(Forest_Path)
    cab = Cabin()
    cab.describe()
    cab.choose_action()
    cab.after_desc()
    ice = Tundra()
    ice.describe()
    ice.choose_action()
    ice.after_desc()
    frozen = Tundra_Path()
    frozen.describe()
    frozen.situational_actions(Tundra_Path)
    water = Ocean()
    water.describe()
    water.choose_action()
    water.after_desc()
    rock = Cave()
    rock.describe()
    rock.choose_action()
    tunnel = Tunnel()
    tunnel.describe()
    tunnel.situational_actions(Tunnel)
    home = House()
    home.describe()
    home.choose_action()
    home.after_desc()
    medical = Hospital()
    medical.describe()
    medical.choose_action()
    medical.after_desc()
main()
