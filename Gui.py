
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

#Function handles all actions of what user selects in combobox using if statements 
def getvalue(combobox, actions, lbl, lbl2, btn, controller):
    value = combobox.get()
    
    if value in actions:
        player.set_act_taken()
        lbl.config(text= actions[value])
        next_button = ttk.Button(master=None, text="Next!",
        command= lambda: [controller.show_frame(Forest_Path),
        next_button.destroy(), player.set_location(), player.update_score()])

        if value == 'location':
            player.set_act_taken()
            lbl.config(text=actions[value] + player.loc_get().zonename())
            lbl2.configure(master=None, text="")

        elif value == 'inventory':
            player.set_act_taken()
            inv_list = tk.Listbox(master=None, selectmode= 'single',)
            inv_list.place(relx=0.51, rely=0.5, anchor='center')
            lbl.configure(text= player.inventory_show(lbl, inv_list))
            use= ttk.Button(master=None, text="use", command= lambda: [player.inventory_use(lbl, inv_list),
            use.destroy(), inv_list.destroy(), btn.destroy()])
            use.place(relx = 0.48, rely= 0.7, anchor='center')
            next_button.place(relx=0.51, rely=0.6, anchor='center')
        
        elif value == 'right':
            player.set_act_taken()
            lbl.configure(text= actions[value])
            player.loc_get().after_desc(lbl2)
            btn.destroy()
            next_button.place(relx= 0.51, rely= 0.6, anchor='center')

        elif value == 'left' and player.loc_get() != locations[1]:
            player.set_act_taken()
            lbl.configure(text= actions[value])
            player.loc_get().after_desc(lbl2)
            btn.destroy()
            next_button.place(relx= 0.51, rely= 0.6, anchor='center')

        elif  value == 'left' and player.loc_get() == locations[1]:
            player.set_act_taken()
            lbl.configure(text=actions[value])
            locations[1].situational(player, lbl2)
            btn.destroy()
            next_button = ttk.Button(master=None, text="Next!",
            command= lambda: [controller.show_frame(loosescreen),
            next_button.destroy(), player.set_location(), player.update_score()])
            next_button.place(relx= 0.51, rely= 0.6, anchor='center')

        elif value == 'score':
            player.set_act_taken()
            lbl.configure(text= actions[value] + str(player.score_return()))
            lbl2.configure(master=None, text="")

        elif value == 'search':
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
        
        player.update_score()
        actions = locations[0].actions
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


class Forest_Path(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Forest Pathway\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= player.loc_get().description, font=LARGE_FONT)
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
        label = tk.Label(self, text= player.loc_get().description, font=LARGE_FONT)
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
        label = tk.Label(self, text= player.loc_get().description, font=LARGE_FONT)
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
        label = tk.Label(self, text= player.loc_get().description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[4].actions
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


class Ocean(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Ocean\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= player.loc_get().description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[5].actions
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
    

class Cave(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Cave\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= player.loc_get().description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[6].actions
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


class Tunnel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Tunnel\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= player.loc_get().description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[7].actions
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


class House(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Forest Pathway\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= player.loc_get().description, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        actions = locations[8].actions
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


class Hospital(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Forest Pathway\n =====================\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text= player.loc_get().description, font=LARGE_FONT)
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
