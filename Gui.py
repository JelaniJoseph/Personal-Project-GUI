
from items import *
from player import *
from zone import *
from project import title
from project import replay
from project import end_screen
import tkinter as tk
from tkinter import ttk


locations = locale_data(backpack,Wisp_in_bottle,coat,coin)
player = Player_Data(locations)
title_screen = title()

LARGE_FONT= ("Verdana", 12)

class BioSagaApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Bio-Saga")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, CharCreation, Forest, Forest_Path):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    # def left_value(self, value_list):
    #         if value_list[0]== 'left':
    #             player.set_act_taken()
    #             value_list[2].configure(text= value_list[6][value_list[0]])
    #             player.loc_get().after_desc(value_list[3])
    #             value_list[4].destroy()
    #             value_list[1].place(relx= 0.51, rely= 0.6, anchor='center')


    # def right_value(self, value_list):
    #     if value_list[0] == 'right':
    #         player.set_act_taken()
    #         value_list[2].configure(text= value_list[6][value_list[0]])
    #         player.loc_get().after_desc(value_list[3])
    #         value_list[4].destroy()
    #         value_list[1].place(relx= 0.51, rely= 0.6, anchor='center')


def getvalue(combobox, actions, lbl, lbl2, btn, controller):
    value = combobox.get()
    
    if value in actions:
        player.set_act_taken()
        lbl.config(text= actions[value])
        next_button = ttk.Button(master=None, text="Next!",
        command= lambda: [controller.show_frame(Forest_Path),
        next_button.destroy(), player.set_location(), player.update_score()])

        if value == 'location':
            print(value)
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

    value_list = [value, next_button, lbl, lbl2, btn, controller, actions]
    return(value_list)


   
 
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome To Bio-Saga!", font=LARGE_FONT)
        label = tk.Label(self, text=title(), font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        btn = ttk.Button(self, text="Begin!", command= lambda: controller.show_frame(CharCreation))
        btn.pack()


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


# def getvalue_fpath(combobox, actions, lbl, lbl2, btn, controller):
#     value = combobox.get()
#     if value in actions:
#         player.set_act_taken()
#         lbl.config(text= actions[value])
#         next_button = ttk.Button(master=None, text="Next!",
#             command= lambda: [controller.show_frame(Forest_Path),
#             next_button.destroy(), player.set_location(), player.update_score()])
#     if value == 'location':
#         player.set_act_taken()
#         lbl.config(text= actions[value] + player.loc_get().zonename())
#         lbl2.configure(master=None, text="")
#     elif value== 'left':
#         player.set_act_taken()
#         lbl.configure(text= actions[value])
#         lbl2.configure(text= player.loc_get().consequence)
#         btn.destroy()
#         next_button.place(relx= 0.51, rely= 0.6, anchor='center')
#     elif value== 'right':
#         player.set_act_taken()
#         lbl.configure(text= actions[value])
#         player.loc_get().after_desc(lbl2)
#         btn.destroy()
#         next_button.place(relx= 0.51, rely= 0.6, anchor='center')
#     elif value == 'inventory':
#         player.set_act_taken()
#         inv_list = tk.Listbox(master=None, selectmode= 'single',)
#         inv_list.place(relx=0.51, rely=0.5, anchor='center')
#         lbl.configure(text= player.inventory_show(lbl, inv_list))
#         use= ttk.Button(master=None, text="use", command= lambda: [player.inventory_use(lbl, inv_list),
#         use.destroy(), inv_list.destroy(), btn.destroy()])
#         use.place(relx = 0.48, rely= 0.7, anchor='center')
#         next_button.place(relx=0.51, rely=0.6, anchor='center')
#     elif value == 'score':
#         player.set_act_taken()
#         lbl.configure(text= actions[value] + str(player.score_return()))
#         lbl2.configure(master=None, text="")
#     elif value == 'search':
#         player.set_act_taken()
#         lbl.configure(text= actions[value])
#         lbl2.configure(master=None, text="would you like to pick up the item?")
#         yes_btn = ttk.Button(master=None, text="Yes", command= lambda:[lbl2.configure(text=""), 
#         player.take(lbl), yes_btn.destroy(), no_btn.destroy(), player.loc_get().after_desc(lbl2),
#             btn.destroy(),
#             next_button.place(relx= 0.51, rely= 0.6, anchor='center')])
#         yes_btn.place(relx=0.4, rely=0.5, anchor= 'center')
#         no_btn = ttk.Button(master=None, text="No", 
#         command= lambda:[player.drop_item(lbl), yes_btn.destroy(), no_btn.destroy(),
#         player.loc_get().after_desc(lbl2), btn.destroy(),
#         next_button.place(relx= 0.51, rely= 0.6, anchor='center')])
#         no_btn.place(relx=0.6, rely=0.5, anchor= 'center')


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
        lbl = ttk.Label(self, text="", font=LARGE_FONT)
        lbl2=ttk.Label(self, text="", font= LARGE_FONT)
        btn= ttk.Button(self, text="Continue!",
        command= lambda: [getvalue(self.box, actions, lbl, lbl2, btn, controller)
        ])
        btn.pack()
        lbl.pack()
        lbl2.pack()

class loosescreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)


app = BioSagaApp()
app.geometry("800x600")
app.mainloop()
