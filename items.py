class Items:

    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use

class Wisp_in_bottle(Items):
    def __init__(self):
        Items.__init__(self, 'A Wisp in a Bottle', 'Will lead you to vicotry!', 1)

class Coat(Items):
    def __init__(self):
        Items.__init__(self, 'Coat', 'Looks nice and warm', 10)

class Backpack(Items):
    def __init__(self):
        Items.__init__(self, 'Red Backpack', 'Looks spacious', 10)

class Coin(Items):
    def __init__(self):
        Items.__init__(self, 'A coin with a skull on it', 'Just looking at it makes you feel uneasy', 1)
