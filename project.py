# Authors: Jelani, and [daniel if he ever accepts the invite :/]
# This program will simulate a text-based game
# Project ver 3
# Date completed 11/6/2019

from player import *
from items import *


def project():
    locations = locale_data(backpack,Wisp_in_bottle,coat,coin)
    player = Player_Data(locations)
    conditional = True
    title()
    playercustom(player)
    game_loop(locations, conditional, player)
    end_screen(player, locations, conditional)
    

# Displays the title screen and Intro
# Allows player to choose username
def title():
    title_display = str('''
    Welcome to Bio-Saga\n
    =========================\n
    Backstory:\n
    You find yourself inside a Forest
    Your head hurts, and you cant remember how you got here.
    You try and remember your name...
    You look around and see that you are surrounded by strange trees.
    Not knowing what else to do or where to go you get up and begin to wander.
    Soon you find a sort of entrance in the forest, you decide to walk in.\n
    Instructions:\n
    Be sure to read carefully, as the list of available commands will be shown to the user.
    type 'Help' to view the commands, 'score' to view current score, and 'quit' to exit the game.\n
    Otherwise, have fun! and thanks for playing Bio-Saga!''')
    print(title_display)
    return(title_display)
# Function allows player to customize themselves, so far its just a name.
def playercustom(player):
    player.setname()


def replay(player, locations, conditional, lbl2):
    print("The game is over, but would you like to replay?")
    replay_choice = input('y/n: ')
    if replay_choice =='y':
        locations = locale_data(backpack,Wisp_in_bottle,coat,coin)
        player = Player_Data(locations)
        BioSagaApp.show_frame(StartPage)
    elif replay_choice =='n':
        lbl2.configure(text= "Thanks for playing!")
        quit()
        replay(player, locations, conditional)


# Main game loop, prints the situation, and based on input locations vary
# Commands available for user are listed before they are asked for input.
def game_loop(locations, conditional, player):
    while conditional == True:
        player.loc_get().describe()
        player.update_score()
        player.loc_get().choose_action(player)
        player.set_location()
        locations[1].describe()
        conditional = locations[1].forest_path_actions(locations, player)
        if conditional == False:
            replay(locations, True, player)
        player.set_location()
        player.update_score()
        locations[2].describe()
        locations[2].choose_action(player)
        player.set_location()
        player.update_score()
        locations[3].describe()
        locations[3].choose_action(player)
        player.set_location()
        player.update_score()
        locations[4].describe()
        conditional = locations[4].tundra_path_actions(locations, player)
        if conditional == False:
            replay(locations, True, player)
        player.set_location()
        player.update_score()
        locations[5].describe()
        locations[5].choose_action(player)
        player.set_location()
        player.update_score()
        locations[6].describe()
        locations[6].choose_action(player)
        player.set_location()
        player.update_score()
        locations[7].describe()
        conditional = locations[7].tunnel_action_option(locations, player)
        if conditional == False:
            replay(locations, True, player)
        player.set_location()
        player.update_score()
        locations[8].describe()
        locations[8].choose_action(player)
        player.set_location()
        player.update_score()
        locations[9].describe()
        locations[9].choose_action(player)
        break


def end_screen(player, locations, conditional):
    print("But then you wonder what was that strange experience you went through and who was that shadowy figure?")
    print("You decide it would be best to think about it later as right now your far too relieved to be alive.")
    print(player.getname(), "Finished the game in:", player.timer(), "steps!")
    print("Copyright: This game was created by Jelani\n")
    print("If you have any questions feel free to email jelani.joseph1@marist.edu")
    replay(player, locations, conditional)
# project()

