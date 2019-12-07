class Items:

    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use


    def getname(self):
        return(self.name)


    def item_use(self):
        self.use -= 1
        return(self.use)


    def itemdisplay(self):
        return(self.description)


    def __str__(self):
        return '{} {} {}'.format(self.name, self.description, self.use)


Wisp_in_bottle = Items('trapped_wisp', 'Will lead you to vicotry!', 1)

backpack = Items('red_backpack', 'Looks spacious', 10)

coat = Items('coat', 'Looks nice and warm', 10)

coin = Items('coin', 'A coin with a skull on it, Just looking at it makes you feel uneasy', 1)
