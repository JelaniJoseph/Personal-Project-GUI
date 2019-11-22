class Zone:
    def __init__(self, name, description, actions, after, **kwargs):
        self.name = name
        self.description = description
        self.after = after
        self.actions = actions
        


    def describe(self):
        print(self.name)
        print("=========")
        print(self.description)

    def after_desc(self):
        print(self.after)

class Forest(Zone):

    def __init__(self):
        Zone.__init__(self, name = "Forest", description = "You enter the Ominous Woods, there seems to be two paths",
        after = "as you walk through the path you hear a sinister roar, it seems your choices will now have consequences.",
        actions = {"left": "You take the left-most path", "right": "You take the right-side path", "Search": "You found a backpack!"})


    def choose_action(self):
        for key, value in self.actions.items():
            print("[]", key)
        action = input("\nAction >> ").lower()
        if action in self.actions:
            print(self.actions[action])




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
    forest.choose_action()
    forest.after_desc()
main()