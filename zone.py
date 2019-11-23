
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

    def after_desc(self):
        print(self.after)

class Forest(Zone):

    def __init__(self):
        Zone.__init__(self, "Forest", "You enter the Ominous Woods, there seems to be two paths",
        {"left": "You take the left-most path", "right": "You take the right-side path", "search": "You found a backpack!"},
        "as you continue you hear a sinister roar, it seems your choices will now have consequences.")


    def choose_action(self, actions_taken, forest):
        while True:
            for key, value in self.actions.items():
                print("[]", key)
            action = input("\nAction >> ").lower()
            actions_taken += 1
            if action in self.actions:
                print(self.actions[action])
                print(Forest.after_desc())
                break
            else:      
                action = input("\n Incorrect, Try Again >>").lower()
            

class Forest_Path(Zone):
    def __init__(self):
        Zone.__init__(self, "Forest", "As you continue through the Forest you see a glint in the trees, and two pathways.", 
        {"right": "You take the right path","left": "You take the left path, but it seems to be a dead end!","search": "You found something"}, 
         "You continue on!")

    def choose_action2(self, actions_taken, Forest_Path):
        while True:
            actions_taken = 0
            for key, value in self.actions.items():
                print("[]", key)
            action = input("\nAction >> ").lower()
            actions_taken += 1
            if action in self.actions:
                print(self.actions[action])
                print(Forest_Path.after_desc())
                break
            else:      
                action = input("\nIncorrect, Try Again >>").lower()

# class Cabin(Zone):
#     def __init__(self):
#         Zone.__init__(self, name = "Cabin", description = "You squint and can barely make out the figure of a log cabin",
#         actions = {"Search": "You found a coat!", "Rest": " You decide to rest a while...",
#             "Find an exit": "You look for a way out of the cabin"})

# class Tundra(Zone):
#     def __init__(self):
#         Zone.__init__(self, name = "Tundra" )
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
    actions_taken = 0
    forest = Forest()
    forest.describe()
    # forest.choose_action(actions_taken, forest)
    forest2 = Forest_Path()
    forest2.describe()
    forest2.choose_action2(Forest_Path, actions_taken)
main()