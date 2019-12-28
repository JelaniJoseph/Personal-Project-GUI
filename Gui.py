
from items import *
from player import *
from zone import *
from project import title
from project import replay
from project import end_screen
import tkinter as tk
from tkinter import ttk

#Instantiation of possible locations, player options and the introduction screen.
locations = locale_data(backpack,Wisp_in_bottle,coat,coin)
player = Player_Data(locations)
title_screen = title()
#Font for styling text 
LARGE_FONT= ("Verdana", 12)
#Is used to create the frame for the user to interact with
class BioSagaApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Bio-Saga")
        #Main function that creates the GUI frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        #For loop that iterates through all possible pages for user to see and shows them
        for F in (StartPage, CharCreation, Forest, Forest_Path, loosescreen,
        Cabin, Tundra, Tundra_Path, Ocean, Cave, Tunnel, House, Hospital):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    # Displays the frames to the user
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#List of if statements that would run under any circumstance unless otherwise stated
def common_functions(conditional, combobox, actions, lbl, lbl2, btn, controller):
    value = combobox.get()
    if value in actions:
        player.set_act_taken()
        lbl.config(text= actions[value])
        # Button to go to next page should only go to forest path and be used in the forest area
        next_button = ttk.Button(master=None, text="Next!",
        command= lambda: [controller.show_frame(Forest_Path),
        next_button.destroy(), player.set_location(), player.update_score()])
        # if user is in forest pathway make it so next button takes user to cabin area
        # And if user selects left while in forest path area make it so user is taken to loose screen 
        if (conditional == True):
            next_button = ttk.Button(master=None, text="Next!",
            command= lambda: [controller.show_frame(Cabin),
            next_button.destroy(), player.set_location(), player.update_score()])
            next_button.place(relx=0.51, rely=0.6, anchor='center')
            if value == 'left':
                next_button.destroy()
                locations[1].situational(player, lbl2)
                next_button = ttk.Button(master=None, text="You Died...",
                command= lambda: [controller.show_frame(loosescreen), next_button.destroy()])
        # if user is in cabin area make it so next button is re-defined and now takes user to Tundra area
        if (conditional == 1):
            next_button = ttk.Button(master=None, text="Next!",
            command= lambda: [controller.show_frame(Tundra),
            next_button.destroy(), player.set_location(), player.update_score()])
            next_button.place(relx=0.51, rely=0.6, anchor='center')
        # if user is in tundra area re-define button and take user to tundra path area
        if (conditional == 2):
            next_button = ttk.Button(master=None, text="Next!",
            command= lambda: [controller.show_frame(Tundra_Path),
            next_button.destroy(), player.set_location(), player.update_score()])
            next_button.place(relx=0.51, rely=0.6, anchor='center')
        # if user does not have coat in inv and tries to do an action take user to loose screen condition
        # if not then allow the user to access next ocean area
        if (conditional == 3):
            if player.loc_get() == locations[4] and coat not in player.inventory:
                btn.destroy()
                locations[4].situational(player, lbl2)
                next_button = ttk.Button(master=None, text="Next!",
                command= lambda: [controller.show_frame(loosescreen),
                next_button.destroy()])
                next_button.place(relx= 0.51, rely= 0.6, anchor='center')
            else:
                next_button = ttk.Button(master=None, text="Next!",
                command= lambda: [controller.show_frame(Ocean),
                next_button.destroy(), player.set_location(), player.update_score()])
                next_button.place(relx=0.51, rely=0.6, anchor='center')
        # if user is in Tunnel area and selects left then take user to loose screen.
        # if not then allow user to access House area
        if (conditional == 4):
            if value == 'left':
                player.set_act_taken()
                lbl.configure(text=actions[value])
                locations[7].situational(player, lbl2)
                btn.destroy()
                next_button = ttk.Button(master=None, text="Next!",
                command= lambda:[controller.show_frame(loosescreen),
                next_button.destroy()])
                next_button.place(relx= 0.51, rely= 0.6, anchor='center')
            else: 
                next_button = ttk.Button(master=None, text="Next!",
                command= lambda: controller.show_frame(House))
                next_button.place(relx= 0.51, rely= 0.6, anchor='center')
        # if user is in area Ocean allow them to access Cave area with swim action
        if (conditional == 5):
            next_button = ttk.Button(master=None, text="Next!",
            command= lambda: controller.show_frame(Cave))
            next_button.place(relx= 0.51, rely= 0.6, anchor='center')
        # if user area is in cave allow them to access Tunnel area with next button
        if (conditional == 6):
            next_button = ttk.Button(master=None, text="Next!",
            command= lambda: controller.show_frame(Tunnel))
            next_button.place(relx= 0.51, rely= 0.6, anchor='center')
        # if user is in tunnel area allow user to access House area with next button
        if (conditional == 7):
            next_button = ttk.Button(master=None, text="Next!",
            command= lambda: controller.show_frame(House))
            next_button.place(relx= 0.51, rely= 0.6, anchor='center')
        # if user is in area house then allow them to access Hospital area with next button
        if (conditional == 8):
            next_button = ttk.Button(master=None, text="Next!",
            command= lambda: controller.show_frame(Hospital))
            next_button.place(relx= 0.51, rely= 0.6, anchor='center')
        # allows user to see their current location
        if value == 'location':
            player.set_act_taken()
            lbl.config(text=actions[value] + player.loc_get().zonename())
            lbl2.configure(master=None, text="")
        # Allows user to view score
        if value == 'score':
            player.set_act_taken()
            lbl.configure(text= actions[value] + str(player.score_return()))
            lbl2.configure(master=None, text="")
        # Allows user to find items and either add them to inventory or discard them if area has search available
        if value == 'search':
            player.set_act_taken()
            lbl.configure(text= actions[value])
            lbl2.configure(master=None, text="would you like to pick up the item?")
            yes_btn = ttk.Button(master=None, text="Yes", command= lambda:[lbl2.configure(text=""), 
            player.take(lbl), yes_btn.destroy(), no_btn.destroy(), player.loc_get().after_desc(lbl2),
                btn.destroy(),
                next_button.place(relx= 0.51, rely= 0.6, anchor='center')])
            yes_btn.place(relx=0.4, rely=0.5, anchor= 'center')
            no_btn = ttk.Button(master=None, text="No", 
            command= lambda:[player.drop_item(lbl), yes_btn.destroy(), no_btn.destroy(),
            player.loc_get().after_desc(lbl2), btn.destroy(),
            next_button.place(relx= 0.51, rely= 0.6, anchor='center')])
            no_btn.place(relx=0.6, rely=0.5, anchor= 'center')
        # allows user to open inventory, select an item, and use the item or return back to selection screen.
        if value == 'inventory':
            player.set_act_taken()
            inv_list = tk.Listbox(master=None, selectmode= 'single',)
            inv_list.place(relx=0.51, rely=0.5, anchor='center')
            lbl.configure(text= player.inventory_show(lbl, inv_list))
            use= ttk.Button(master=None, text="use", command= lambda: [player.inventory_use(lbl, inv_list),
            use.destroy(), inv_list.destroy(), btn.destroy()])
            use.place(relx = 0.48, rely= 0.7, anchor='center')
            next_button.place(relx=0.51, rely=0.6, anchor='center')
        # lets user take a right path
        if value == 'right':
            player.set_act_taken()
            lbl.configure(text= actions[value])
            player.loc_get().after_desc(lbl2)
            btn.destroy()
            next_button.place(relx= 0.51, rely= 0.6, anchor='center')
        # lets user take a left path
        if value == 'left':
            player.set_act_taken()
            lbl.configure(text= actions[value])
            player.loc_get().after_desc(lbl2)
            btn.destroy()
            next_button.place(relx= 0.51, rely= 0.6, anchor='center')
        # if user selects this option which is only available in Tundra_Path, lead to loose screen
        if value == 'fight':
            player.set_act_taken()
            lbl.configure(text= actions[value])
            locations[4].situational(player, lbl2)
            btn.destroy()
            next_button = ttk.Button(master=None, text="Next!",
            command= lambda: [controller.show_frame(loosescreen),
            next_button.destroy()])

#Function handles all actions of what user selects in combobox using if statements 
def getvalue(combobox, actions, lbl, lbl2, btn, controller):
        area = player.loc_get()
        # if user is in forest_pathway then run this
        if (area == locations[1]):
            common_functions(True,combobox, actions, lbl, lbl2, btn, controller)
        # if user is in Cabin then play this
        if (area == locations[2]):
            common_functions(1,combobox, actions, lbl, lbl2, btn, controller)
        # if user is in Tundra then play this
        if (area == locations[3]):
            common_functions(2,combobox, actions, lbl, lbl2, btn, controller)
        # if user is in Tundra_Path then play this
        if (area == locations[4]):
            common_functions(3,combobox, actions, lbl, lbl2, btn, controller)
        # if user is in cave then play this
        if (area == locations[7]):
            common_functions(4,combobox, actions, lbl, lbl2, btn, controller)
        # if user is in Ocean then play this
        if (area == locations[5]):
            common_functions(5,combobox, actions, lbl, lbl2, btn, controller)
        # if user is in Cave then play this
        if (area == locations[6]):
            common_functions(6,combobox, actions, lbl, lbl2, btn, controller)
        # if user is in House then play this
        if (area == locations[8]):
            common_functions(7,combobox, actions, lbl, lbl2, btn, controller)
        # if user is in Hospital then play this
        if (area == locations[9]):
            common_functions(8,combobox, actions, lbl, lbl2, btn, controller)
        # if none of the above is true then perform normal functionality
        else:
            common_functions(False,combobox, actions, lbl, lbl2, btn, controller)

# First page the user sees displays title and prompts user to continue to next page
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome To Bio-Saga!", font=LARGE_FONT)
        label = tk.Label(self, text=title(), font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        btn = ttk.Button(self, text="Begin!", command= lambda: controller.show_frame(CharCreation))
        btn.pack()

# Allows user to customize their character by naming them
class CharCreation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Character Creation\n =====================\n Enter your username Below!",
         font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        username = ttk.Entry(self)
        username.get()
        username.pack(pady=10,padx=10)
        btn = ttk.Button(self, text="Start", command= lambda: controller.show_frame(Forest))
        btn.pack()
        
# first location in the game all below create a combobox list based on dictionary actions which are defined
# within each separate location then based on user selection labels are configured.
class Forest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Forest\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text=locations[0].description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        #begins player score update, and creates option box for user to select from then places it on screen.
        player.update_score()
        actions = locations[0].actions
        self.box = ttk.Combobox(self, values=list(actions.keys()), state="readonly", justify="center")
        self.box.bind("<<ComboboxSelected>>")
        self.box.pack(pady=10,padx=10)
        # Creates button to let action play through this is how the program takes user action
        btn= ttk.Button(self, text="Continue!", 
        command= lambda: [getvalue(self.box, actions, lbl, lbl2, btn, controller)])
        # places the descriptions of the user area and / or action description
        lbl = ttk.Label(self, text="", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)

        btn.pack(pady=10, padx=10)
        lbl.pack()
        lbl2.pack()


class Forest_Path(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Forest Pathway\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= locations[1].description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[1].actions
        self.box = ttk.Combobox(self, values=list(actions.keys()), state="readonly", justify="center")
        self.box.bind("<<ComboboxSelected>>")
        self.box.pack(pady=10,padx=10)

 
        btn= ttk.Button(self, text="Continue!",
        command= lambda: [getvalue(self.box, actions, lbl, lbl2, btn, controller)])

        lbl = ttk.Label(self, text="", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)
        
        btn.pack(pady=10, padx=10)
        lbl.pack()
        lbl2.pack()


class Cabin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Cabin\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= locations[2].description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[2].actions
        self.box = ttk.Combobox(self, values=list(actions.keys()), state="readonly", justify="center")
        self.box.bind("<<ComboboxSelected>>")
        self.box.pack(pady=10,padx=10)

        btn= ttk.Button(self, text="Continue!",
        command= lambda: [getvalue(self.box, actions, lbl, lbl2, btn, controller)])
        
        lbl = ttk.Label(self, text="", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)
        
        btn.pack(pady=10, padx=10)
        lbl.pack()
        lbl2.pack()


class Tundra(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Tundra\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= locations[3].description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[3].actions
        self.box = ttk.Combobox(self, values=list(actions.keys()), state="readonly", justify="center")
        self.box.bind("<<ComboboxSelected>>")
        self.box.pack(pady=10,padx=10)

        
        
        btn= ttk.Button(self, text="Continue!",
        command= lambda: [getvalue(self.box, actions, lbl, lbl2, btn, controller)])

        lbl = ttk.Label(self, text="", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)
        
        btn.pack(pady=10, padx=10)
        lbl.pack()
        lbl2.pack()


class Tundra_Path(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Tundra Pathway\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= locations[4].description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[4].actions
        self.box = ttk.Combobox(self, values=list(actions.keys()), state="readonly", justify="center")
        self.box.bind("<<ComboboxSelected>>")
        self.box.pack(pady=10,padx=10)

        next_button = ttk.Button(self, text="Begin!", command= lambda: [controller.show_frame(Tundra),
        next_button.destroy(), player.set_location(), player.update_score()])

        btn= ttk.Button(self, text="Continue!",
        command= lambda: [getvalue(self.box, actions, lbl, lbl2, btn, controller)])

        lbl = ttk.Label(self, text="", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)
        
        btn.pack(pady=10, padx=10)
        lbl.pack()
        lbl2.pack()


class Ocean(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Ocean\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= locations[5].description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[5].actions
        self.box = ttk.Combobox(self, values=list(actions.keys()), state="readonly", justify="center")
        self.box.bind("<<ComboboxSelected>>")
        self.box.pack(pady=10,padx=10)

        next_button = ttk.Button(self, text="Begin!", command= lambda: [controller.show_frame(Tundra),
        next_button.destroy(), player.set_location(), player.update_score()])

        btn= ttk.Button(self, text="Continue!",
        command= lambda: [getvalue(self.box, actions, lbl, lbl2, btn, controller)])

        lbl = ttk.Label(self, text="", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)
        
        btn.pack(pady=10, padx=10)
        lbl.pack()
        lbl2.pack()
    

class Cave(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Cave\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= locations[6].description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[6].actions
        self.box = ttk.Combobox(self, values=list(actions.keys()), state="readonly", justify="center")
        self.box.bind("<<ComboboxSelected>>")
        self.box.pack(pady=10,padx=10)

        next_button = ttk.Button(self, text="Begin!", command= lambda: [controller.show_frame(Tundra),
        next_button.destroy(), player.set_location(), player.update_score()])

        btn= ttk.Button(self, text="Continue!",
        command= lambda: [getvalue(self.box, actions, lbl, lbl2, btn, controller)])

        lbl = ttk.Label(self, text="", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)
        
        btn.pack(pady=10, padx=10)
        lbl.pack()
        lbl2.pack()


class Tunnel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Tunnel\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= locations[7].description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[7].actions
        self.box = ttk.Combobox(self, values=list(actions.keys()), state="readonly", justify="center")
        self.box.bind("<<ComboboxSelected>>")
        self.box.pack(pady=10,padx=10)

        next_button = ttk.Button(self, text="Begin!", command= lambda: [controller.show_frame(Tundra),
        next_button.destroy(), player.set_location(), player.update_score()])

        btn= ttk.Button(self, text="Continue!",
        command= lambda: [getvalue(self.box, actions, lbl, lbl2, btn, controller)])

        lbl = ttk.Label(self, text="", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)
        
        btn.pack(pady=10, padx=10)
        lbl.pack()
        lbl2.pack()


class House(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="House\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= locations[8].description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[8].actions
        self.box = ttk.Combobox(self, values=list(actions.keys()), state="readonly", justify="center")
        self.box.bind("<<ComboboxSelected>>")
        self.box.pack(pady=10,padx=10)

        next_button = ttk.Button(self, text="Begin!", command= lambda: [controller.show_frame(Tundra),
        next_button.destroy(), player.set_location(), player.update_score()])
        
        btn= ttk.Button(self, text="Continue!",
        command= lambda: [getvalue(self.box, actions, lbl, lbl2, btn, controller)])

        lbl = ttk.Label(self, text="", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)
        
        btn.pack(pady=10, padx=10)
        lbl.pack()
        lbl2.pack()


class Hospital(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Hospital\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= locations[9].description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[9].actions
        self.box = ttk.Combobox(self, values=list(actions.keys()), state="readonly", justify="center")
        self.box.bind("<<ComboboxSelected>>")
        self.box.pack(pady=10,padx=10)

        btn= ttk.Button(self, text="Continue!",
        command= lambda: [getvalue(self.box, actions, lbl, lbl2, btn, controller)])

        lbl = ttk.Label(self, text="", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)
        
        btn.pack(pady=10, padx=10)
        lbl.pack()
        lbl2.pack()

# screen that should only show when user selects wrong option gives option to replay game or quit completely
class loosescreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.label = tk.Label(self, text="Game Over\n =====================\n", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)

        lbl = ttk.Label(self, text="The game is over, but would you like to replay?", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)

        loose_btn = ttk.Button(self, text= "Yes", command= lambda: [replay(player, locations),
        controller.show_frame(StartPage), ])
        quit_btn = ttk.Button(self, text="No", command= lambda: quit())
        lbl.pack()
        lbl2.pack()
        loose_btn.pack()
        quit_btn.pack()


app = BioSagaApp()
app.geometry("800x600")
app.mainloop()
