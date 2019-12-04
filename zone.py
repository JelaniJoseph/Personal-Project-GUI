from items import *
class Zone:
    def __init__(self, name, description, after, consequence, item_list, actions):
        self.name = name
        self.description = description
        self.after = after
        self.consequence = consequence
        self.item_list = item_list
        self.visited = False
        self.searched = False
        self.actions = actions



    def describe(self):
        print(self.name)
        print("=========")
        print(self.description)


    def choose_action(self, player):
        for key, value in self.actions.items():
            print("[]", key.capitalize())
        action = input("\nAction >> ").lower()
        if action in self.actions and action != 'location'  and action != 'score':
            print(self.actions[action])
            player.set_act_taken()
            self.visited = True
            print(self.after_desc())
            if action  == 'search':
                print(self.actions[action])
                player.set_act_taken()
                self.searched == True
                print("what will", player.getname(), "do with the item?")
                print("Type 'take' to take the item, or 'drop' to leave it behind!")
                decide = input("take, or drop? ")
                if decide == 'take':
                    player.take()
                    player.set_act_taken()
                    player.inventory_show()
                elif decide == 'drop':
                    print(player.drop_item())
                    player.set_act_taken()
                else:
                    decide = ("Try again, take or drop?")
        elif action == 'location':
            print(self.actions[action] + self.name)
            player.set_act_taken()
            self.choose_action(player)
        elif action == 'score':
            print(player.getname(), "score is: ", player.score_return())
        else:
            print("Inccorrect action, Try again")
            player.set_act_taken()
            self.choose_action(player)

    # function should add item to list within the class
    def add_item(self, item_list):
        item_list.append(Items)

    # should print the item in that locale list
    def get_item_list(self):
        return(self.item_list)


    def area_visited(self):
        if self.visited == True:
            print("Playername has visited: ", self.name)


    def was_searched(self):
        if self.searched == True:
            print("You have searched this locale")

    def after_desc(self):
        print(self.after)


    def situational(self, action):
        print(self.actions[action])
        print(self.consequence)
        print("You Died...\n")
        quit()

  

    def situational_actions(self, Forest_Path, player):
        try:
            for key, value in self.actions.items():
                print("[]", key.capitalize())
            action = input("\nAction >> ").lower()
            player.set_act_taken()
            if action in self.actions and action != action in self.actions['left']:
                print(self.actions[action])
                player.set_act_taken()
                Forest_Path.after_desc(self)
            elif action == action in self.actions['left']:
                player.set_act_taken()
                Forest_Path.situational(self, action)
        except KeyError:
            action = input("\n Incorrect, Try Again >>").lower()
            player.set_act_taken()
            self.situational_actions(Forest_Path, player)


    def situational_actions(self, Tundra_Path, player):
        try:
            for key, value in self.actions.items():
                print("[]", key.capitalize())
            action = input("\nAction >> ").lower()
            if action in self.actions and action != action in self.actions['fight']:
                print(self.actions[action])
                player.set_act_taken()
                Tundra_Path.after_desc(self)
            elif action == action in self.actions['fight']:
                Tundra_Path.situational(self, action)
                player.set_act_taken()
        except KeyError:
            action = input("\n Incorrect, Try Again >>").lower()
            player.set_act_taken()
            self.situational_actions(Tundra_Path, player)


    def situational_actions(self, Tunnel, player):
        try:
            for key, value in self.actions.items():
                print("[]", key.capitalize())
            action = input("\nAction >> ").lower()
            if action in self.actions and action != action in self.actions['left']:
                print(self.actions[action])
                player.set_act_taken()
                Tunnel.after_desc(self)
            elif action == action in self.actions['left']:
                Tunnel.situational(self, action)
                player.set_act_taken()
        except KeyError:
            action = input("\n Incorrect, Try Again >>").lower()
            player.set_act_taken()
            self.situational_actions(Tunnel, player)

def location_test(backpack, Wisp_in_bottle, coat, coin):
    Forest = Zone(name="Forest",description= "You enter the Ominous Woods, there seems to be two paths",
    after="as you continue you hear a sinister roar, it seems your choices will now have consequences.\n",
    consequence= "text is within here", item_list= [backpack], 
    actions= {"left": "You take the left-most path",
        "right": "You take the right-side path", "search": "You found a backpack!",
        'location': "You are in: ", 'score': "Your score is: "})
    Forest_Path = Zone("Forest Pathway", 
    "As you continue through the Forest you see a glint in the trees, and two pathways.", "You continue on!\n", 
        "A pitch black humanoid creature with a smile appears, and kills you", [coin], 
        {"right": "You take the right path", "left": "You take the left path, but it seems to be a dead end!",
        "search": "You found a strange coin"})
    Cabin = Zone("Cabin", "You squint and can barely make out the figure of a log cabin", 
    "You prepare yourself, and push forward!\n", "text", [coat, Wisp_in_bottle],
        {"search": "You found a coat, and a strange flask!",
        "rest": " You decide to rest a while...", "find an exit": "You look for a way out of the cabin"})
    Tundra = Zone("Tundra", "The cold chips away at your very being",
        "After some time you reach an icy lake\n", "text", [None],
        {"walk": "You try to push through the blizzard", 
        "inventory": "you use the wisp in a bottle!", "map": 
        "You open the map and see the pathway you must follow",
        "backward": "it's too cold, you go back in the cabin"})
    Tundra_Path = Zone("Tundra", "as you stare ath the ocean, you hear something dangerous approaching you"
    , "You sink into the icy depths of the water",
        "you lay there bleeding out, and cold.", [None], 
        {"jump": "Afraid for your life you jump into the ocean", 
        "fight": "you stand your ground!, but the monster claps you"})
    Ocean = Zone("Ocean", "you're underwater",
    "As you enter the cave, the entrance behind you closes and the water dissapears", "text", [None],
    {"swim": "you swim downwards and reach an underwater cave"})
    Cave = Zone("Cave", "the area somehow feels alive...", 
        "it's almost as if the area is shifting all on its own...", "text", [None],
        {"look": "as you take in the environment, looking closely at the stalagmites and the rough walls, you find a slot to insert some sort of coin",
        "continue": "you walk down the cave and soon find yourself in a series of tunnels"})
    Tunnel = Zone("Tunnel", "it's dark and you can sense something folowing you",
    "Soon you see a bright light and as you go towards it your area begins to change.",
    "You feel the tunnel begin to move and soon you are enveloped by the floor", [None],
    {"map": "You pull out the map and see that you must make a right turn", 
    "left": "You take the left-most path, but its a dead end...",
        "right": "you take the right-most path"})
    House = Zone("House", "Feels safe and cozy...", "Suddenly, something feels strange...",
        "text", [None], {"wander": "you begin to look in all of the rooms",
        "rest": "you decide to sit down and rest for a while"})
    Hospital = Zone("Hospital", "strangely feels more real than what just happened...", "Everything is finally over",
        "text", [None], {"waken": "You open your eyes and realize that you are now in a hospital"})
    locations = [Forest, Forest_Path, Cabin, Tundra, Tundra_Path, Ocean, Cave, Tunnel, House, Hospital]
    return(locations)