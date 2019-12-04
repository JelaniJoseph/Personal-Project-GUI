class Items:

    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use

    def get_name(self):
        return(self.name)


    def __str__(self):
        return '{} {} {}'.format(self.name, self.description, self.use)

Wisp_in_bottle = Items(name = 'A Wisp in a Bottle', description= 'Will lead you to vicotry!', use= 1)

backpack = Items('Red Backpack', 'Looks spacious', 10)

coat = Items('Coat', 'Looks nice and warm', 10)

coin = Items('A coin with a skull on it', 'Just looking at it makes you feel uneasy', 1)
