class Zone:
    def __init__(self, name, description, actions, after):
        self.name = name
        self.description = description
        self.actions = actions
        self.after = after
        self.actions_taken = 0

    def describe(self):
        print(self.name)
        print("=========")
        print(self.description)

    def choose_action(self):
        while True:
            for key, value in self.actions.items():
                print("[]", key.capitalize())
            action = input("\nAction >> ").lower()
            if action in self.actions:
                print(self.actions[action])
                return(True)
            else:      
                action = input("\n Incorrect, Try Again >>").lower()

    def after_desc(self):
        print(self.after)

class Forest(Zone):

    def __init__(self):
        Zone.__init__(self, "Forest", "You enter the Ominous Woods, there seems to be two paths",
        {"left": "You take the left-most path", "right": "You take the right-side path", "search": "You found a backpack!"},
        "as you continue you hear a sinister roar, it seems your choices will now have consequences.\n")


class Forest_Path(Zone):
    def __init__(self):
        Zone.__init__(self, "Forest Pathway", "As you continue through the Forest you see a glint in the trees, and two pathways.", 
        {"right": "You take the right path","left": "You take the left path, but it seems to be a dead end!", "search": "You found something"}, 
         "You continue on!\n")


class Cabin(Zone):
    def __init__(self):
        Zone.__init__(self, "Cabin", "You squint and can barely make out the figure of a log cabin",
        {"search": "You found a coat, and a map!", "rest": " You decide to rest a while...",
        "find an exit": "You look for a way out of the cabin"}, "You prepare yourself, and push forward!\n")


class Tundra(Zone):
    def __init__(self):
        Zone.__init__(self, "Tundra", "The cold chips away at your very being",
         {"walk": "You try to push through the blizzard", "inventory": "within the backpack there was a wisp in a bottle!",
         "map": "You open the map and see the pathway you must follow","backward": "it's too cold, you go back in the cabin",},
         "After some time you reach an icy lake\n" )


class Tundra_Path(Zone):
    def __init__(self):
        Zone.__init__(self, "Tundra", "as you stare ath the ocean, you hear something dangerous approaching you",
        {"jump": "Afraid for your life you jump into the ocean",
         "fight": "you stand your ground!, but the monster claps you"}, "You sink into the icy depths of the water")


# class Ocean(Zone):
#     def __init__(self):
#         Zone.__init__(self, name = "Ocean" )

# class Cave(Zone):
#     def __init__(self):
#         Zone.__init__(self, name = "Cave" )

# class Tunnel(Zone):
#     def __init__(self):
#         Zone.__init__(self, name = "Tunnel" )

# class House(Zone):
#     def __init__(self):
#         Zone.__init__(self, name = "House" )
# class Hospital(Zone):
#     def __init__(self):
#         Zone.__init__(self, name = "Hospital" )
    

def main():
    forest = Forest()
    forest.describe()
    forest.choose_action()
    forest.after_desc()
    forest2 = Forest_Path()
    forest2.describe()
    forest2.choose_action()
    forest2.after_desc()
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
    frozen.choose_action()
    frozen.after_desc()
main()