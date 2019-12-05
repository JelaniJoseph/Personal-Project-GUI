# Authors: Jelani, and [daniel if he ever accepts the invite :/]
# This program will simulate a text-based game
# Project ver 3
# Date completed 11/6/2019

from player import *
from items import *


def project():
    locations = locale_data(backpack,Wisp_in_bottle,coat,coin)
    player = Player_Data(locations)
    title(locations)
    player = Player_Data(locations)
    playercustom(player)
    game_loop(locations, player)
    email_jel = str("jelani.joseph1@marist.edu")
    end_screen(email_jel, player)


# Displays the title screen and Intro
# Allows player to choose username
def title(locations):
    print("Welcome to Bio-Saga")
    print("=========================\n")
    print("Backstory:\n")
    print("You find yourself inside a Forest")
    print("Your head hurts, and you cant remember how you got here.")
    print("You try and remember your name...")
    print("You look around and see that you are surrounded by strange trees.")
    print("Not knowing what else to do or where to go you get up and begin to wander.")
    print("Soon you find a sort of entrance in the forest, you decide to walk in.\n")
    print("Instructions:\n")
    print("Be sure to read carefully, as the list of available commands will be shown to the user.")
    print("type 'Help' to view the commands, 'score' to view current score, and 'quit' to exit the game.\n")
    print("Otherwise, have fun! and thanks for playing Bio-Saga!")
    input("Press Enter to Start\n")


# Function allows player to customize themselves, so far its just a name.
def playercustom(player):
    player.setname()


# Function to add to score, and show location visited
def goto(player, score, locations):
    score = player.update_score()
    player.next_loc(locations)
    return(score)


# Function takes user input and returns input against the available commands
# After 10 inputs the user will "run out of time" and will be exited out of the loop
def get_int(user, actions, player, actions_taken):
    player.timer(actions, actions_taken)


# Main game loop, prints the situation, and based on input locations vary
# Commands available for user are listed before they are asked for input.
def game_loop(locations, player):
    while True:
        player.loc_get().describe()
        player.update_score()
        player.loc_get().choose_action(player)
        player.set_location()
        locations[1].describe()
        locations[1].forest_path_actions(locations, player)
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
        locations[4].tundra_path_actions(locations, player)
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
        locations[7].tunnel_action_option(locations, player)
        player.set_location()
        player.update_score()
        locations[8].describe()
        locations[8].choose_action(player)
        player.set_location()
        player.update_score()
        locations[9].describe()
        locations[9].choose_action(player)

project()


def end_screen(email_jel, player):
    print("But then you wonder what was that strange experience you went through and who was that shadowy figure?")
    print("You decide it would be best to think about it later as right now your far too relieved to be alive.")
    player.timer()
    print("Copyright: This game was created by Jelani, and Daniel\n")
    print("If you have any questions feel free to email " + email_jel)
    return(email_jel)