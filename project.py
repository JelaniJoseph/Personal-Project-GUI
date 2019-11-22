# Authors: Jelani, and [daniel if he ever accepts the invite :/]
# This program will simulate a text-based game
# Project ver 3
# Date completed 11/6/2019

from player import *


def project():
    locations = ['forest', 'Cabin', 'Tundra', 'Ocean', 'Cave', 'Tunnel', 'House', 'Hospital']
    track_loc = [False, False, False, False, False, False, False, False]
    actions = ['take', 'use', 'drop', 'look', 'examine', 'Inventory', 'forward', 'left', 'right', 'quit', 'help', 'points', 'yes', 'no']
    score = 0
    actions_taken = 0
    current_locale = locations[0]
    title(locations)
    player = Player_Data(current_locale, actions)
    playercustom(player)
    game_loop(locations, track_loc, player, score, actions_taken, actions)
    email_jel = str("jelani.joseph1@marist.edu")
    end_screen(email_jel, actions_taken)


# Displays the title screen and Intro
# Allows player to choose username
def title(locations):
    print("Welcome to Bio-Saga")
    print("=========================\n")
    print("Backstory:\n")
    print("You find yourself inside a", locations[0])
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
def game_loop(locations, track_loc, player, score, actions_taken, actions):
    while True:
        print("As you enter the strange", locations[0], "you feel as if your being watched....")
        print("cold, and confused you continue trying to find some clues as to where you are.")
        print("As you walk you come across a winding path with three possible paths.\n")
        print("How will you advance?")
        print("You can go forward, left, or right.")
        choice = player.timer(actions, actions_taken)
        if choice == 'forward':
            print("You decide to keep walking forward. ")
        elif choice == 'left':
            print("You decide to take the left path, and begin to walk. ")
        elif choice == 'right':
            print("You decide to take the right path, and begin to walk. ")
        elif choice == 'points':
            print("Your current score is: ", score)
            choice = player.timer(actions, actions_taken)
        elif choice == 'quit':
            print("exiting game")
            exit()
        elif choice == 'help':
            print("the commands are:", actions)
            print("Otherwise 'quit' to exit the game.\n")
            choice = player.timer(actions, actions_taken)
        else:
           choice = player.timer(actions, actions_taken)
        print("you soon arrive at  another area of the forest, the trees somehow seem more sinister")
        print("You start to notice that the forest has gone completely silent,")
        print("a low roar can be heard in the distance, it would be best to consider which ")
        print("path you choose from now on...\n")
        goto(player, score, locations)
        print("While walking you begin to wonder why it is you cant remember anything")
        print("the last thing you can remember was waking up in this forest in pain")
        print("You stop moving, and begin to try thinking about the situation and how")
        print("you plan to find out about your past")
        print("Suddenly, the low roaring sound begins to pick up")
        print("whatever is making that noise seems to be approaching you at an alarming rate")
        print(player.getname(), "decides it would be best to continue as fast as possible")
        print("as", player.getname(), "starts to jog they come across another split passage")
        print("This time the passage only has two routes, forward or right.")
        choice = player.timer(actions, actions_taken)
        if choice == 'forward':
            print("You decide it would be best to go straight ahead!")
            print("You dash in without a second thought and soon the path becomes extremely dark")
            print("A feeling of dread overwhelms you as that feeling of being watched grows stronger")
            print("Stopping in your tracks you see a shadow looming over you and a hand raises")
            print("You feel a sharp pain in your back and begin to loose conscienceness as you hear soft laughter.\n")
            print("You Died...")
            print(actions_taken)
            exit()
        elif choice == 'right':
            print("You choose the right-most path!")
        elif choice == 'quit':
            print("exiting game")
            exit()
        elif choice == 'help':
            print("the commands are: 'forward', 'right', 'left', 'points', and 'map'.")
            print("Otherwise 'quit' to exit the game.")
            choice = player.timer(actions, actions_taken)
            continue
        elif choice == 'points':
            print("Your current score is: ", score)
            choice = player.timer(actions, actions_taken)
        else:
            choice = player.timer(actions, actions_taken)
        print("As you walk along the path with a hastened pace you see something in the distance")
        print("You squint and can barely make out the figure of a log cabin")
        print("while you gaze at the log cabin a roar heard in the distance catches your attention")
        print("Whatever it is thats approaching its even close than before you decide to hide out in the cabin")
        print(player.getname(), " leaves now enters the", locations[1], ".\n")
        goto(player, score, locations)
        print("As you enter", locations[1], "you feel slightly safer")
        print("You decide that now is a good time to think about the situation")
        print("While your lost in deep thought trying to remember anything you have a vision")
        print("In this vision you see a strange being entering the cabin wearing winter gear, exhausted.")
        print("As you take of your winter gear in this vision you see the being pull up a chair and sit down")
        print("The being then opens up a drawer next to the table and pulls out a large piece of paper")
        print("Suddenly the vision is interrupted by the sound of something hitting the cabin")
        print("remembering the vision you decide it would be best to inspect the drawer")
        print("You open the drawer next to the table and see something inside, its just like in the vision.")
        print("You open the paper, and soon realize that its a map of the area!")
        print("Remember, when you want to look at the map simply type in 'map' to see where you are")
        print("After getting the map you decide it would be best to keep it on you and head out")
        print("You get up and head to the backdoor, you open it expecting to see the forest again")
        print("Except that its no longer a forest, its actually now a", locations[2])
        print("Freezing, and confused you try and look at your surrounding area to see where to go")
        print("You see that your only  way to go is either forward, or check the map")
        print("Afterall theres no point in wandering aimlessly!\n")
        goto(player, score, locations)
        choice = player.timer(actions, actions_taken)
        if choice == 'forward':
            print("you decide to go straight ahead unknowing the dangers that lie ahead!")
            print(" as you start to trudge on you begin to suffer from frostbite ")
            print("Freezing, you start to shake and desperately desire shelter")
            print("You head back to", locations[2], "in order to warm back up")
            print("You decide it would probably be best to look at the map before heading out.")
        elif choice == 'quit':
            print("exiting game")
            exit()
        elif choice == 'points':
            print("Current score: ", score)
            choice = player.timer(actions, actions_taken)
        elif choice == 'help':
            print("the commands are: 'forward', 'right', 'left', 'points', and 'map'.")
            print("Otherwise 'quit' to exit the game.")
            choice = player.timer(actions, actions_taken)
        elif choice == 'map':
            print("+============+\n"
                  "|   •••••    |"
                  "|   •   •    |"
                  "|_|◘|   •    |"
                  "| x |   •••••◘"
                  "+============+")
            print("You see that the best path to take and memorize it")
            print("before you leave you remember the winter gear from the past vision")
            print("after scavenging around for a few minuets you find the gear and equip it")
            print(player.getname(), "walks out of the house and begins to follow the path.")
        else:
            choice = player.timer(actions, actions_taken)
        print("After following the path you soon find yourself in-front of a large", locations[3])
        print("You skeptically look at the water and suddenly while looking at your reflection you remember something.")
        print("You see another vision but this time the being is jumping into the freezing water and swiming down to")
        print("what seems to be a cave about twenty feet in the water.")
        print("you snap out of the vision and think that theres no way your going to jump into the")
        print("freezing water, you'll surely get hypothermia.")
        print("you turn around to go back to the cabin when you feel a presence next to you")
        print("it seems to be a hulking white beast standing on two legs with horns")
        print("while staring at the beast you device a plan, it would be best to either dive in.")
        print("the beings yellow eyes look down upon you and it starts to drool, you must act quickly!\n")
        print("will you dive into the water?")
        choice = player.timer(actions, actions_taken)
        if choice == 'yes':
            continue
        elif choice == 'no':
            print("You cant bring yourself to dive into the water!")
            print("The beast pounces on you and rips you to bloody pieces\n")
            print("You Died...")
            print(player.counter_return)
            exit()
        else:
            choice = player.timer(actions, actions_taken)
        goto(player, score, locations)
        print("With your burst of adrenaline you swim as fast as you can downards like you saw in the vision")
        print("While swimming you feel as if a presence is coming after you, you quicken your pace")
        print("Soon you enter the", locations[4], "and the entrance seals, whatever behind it also being blocked off")
        print("the water dissapears from within it and you can breathe")
        print("you pick yourself up and shed your wintergear, as the cave is oddly humid and warm")
        print("you look around and notice a wired pattern on the wall")
        print("it seems to show arrows pointing in various directions")
        print("it reads: forward, right")
        print("you decide it would be best to memorize this pattern.")
        print("As you advance you come across three pathways, it seems you must choose one to go on.")
        goto(player, score, locations)
        choice = player.timer(actions, actions_taken)
        if choice == 'do':
            print("You dodge the creature, after enhancing yourself it charges past you, and through a wall")
            print("It bursts through the wall and falls to its death.")
        elif choice == 'quit':
            print("exiting game")
            exit()
        elif choice == 'help':
            print("the commands are: 'forward', 'right', 'left', 'points', and 'map'.")
            print("Otherwise 'quit' to exit the game.")
            choice = player.timer(actions, actions_taken)
        elif choice == 'df':
            print("You cast a strong barrier as the beast charges")
            print("It slams its head against the barrier but it is too dense to be broken")
            print("The beast shatters it skull against your barrier and dies")
        elif choice == 'at':
            print("You charge a fire blast and fire away at the beast!")
            print("you seem to hit a vital spot and the beast looses control of its direction")
            print("The beast falls down and bleeds out, it wont be moving anytime soon.")
        else:
            choice = player.timer(actions, actions_taken)
        print("This time you are lead to another clearing with another pathway")
        print("Seems this cave operates much like a maze, you prepare yourself to advance.\n")
        choice = player.timer(actions, actions_taken)
        if choice == 'forward':
            print("You decide to go forward, as you walk down the path in the cave you see a light.")
            print("excitedly you run towards it hoping its a way out.")
            print("As you pass through the exit you find yourself back at", locations[4], ".")
            print("seems that straight was not the correct path...")
        elif choice == 'right':
            print("You cast a strong barrier as the beast charges")
            print("It slams its head against the barrier but it is too dense to be broken")
            print("The beast shatters it skull against your barrier and dies")
        elif choice == 'left':
            print("You cast a strong barrier as the beast charges")
            print("It slams its head against the barrier but it is too dense to be broken")
            print("The beast shatters it skull against your barrier and dies")
        elif choice == 'points':
            print("Your current score is:", score)
            choice = player.timer(actions, actions_taken)
        elif choice == 'help':
            print("the commands are: 'forward', 'right', 'left', 'points', and 'map'.")
            print("Otherwise 'quit' to exit the game.")
            choice = player.timer(actions, actions_taken)
        elif choice == 'quit':
            print("exiting game")
            exit()
        else:
            choice = player.timer(actions, actions_taken)
        print("You take the path and now exit", locations[4], "You now enter", locations[5], ".")
        goto(player, score, locations)
        print("This", locations[5], "seems man made and well taken care of.")
        print("you look down both ways and see nothing, the cost looks clear but where should you go from here.")
        print("as you sit down to think about your next move your hand touches something warm")
        print("looking down you see that it is a red colored rock that emits heat")
        print("as soon as you realize this another vision comes to you")
        print("In this vision the same strange being is in the tunnel and takes the forward path")
        print("the being reaches a staircase at the end and begins to go up, then the vision fades")
        print("Since the visions have lead you to the right places so far you decide to")
        print("follow this one without second question.")
        print("after some time walking in the same direction in the tunnel you see a staircase and decide to go up")
        print("After going up you reach a trapdoor, you open it and find yourself in an oddly familiar place")
        print("You are now in what seems to be a", locations[6], ".")
        goto(player, score, locations)
        print("You decide it would be a good time to rest from the long journey")
        print("As you sit down in a chair you begin to drift off into sleep.")
        print("while sleeping you have a dream, and in this dream you see the strange being from the past visions")
        print("this time however, it seems to be trying to speak to you but its voice is so quiet")
        print("you try your hardest to listen in, and your able to make out a few words.")
        print("???: Wake up, you are in grave danger")
        print("confused you try to ask what exactly the being means and how is it that you keep seeing them")
        print("the being is unresponsive, you then notice that the being begins to smile.")
        print("Suddenly the dream ends and you're awoken by a unsettling sound.")
        print("you open your eyes and realize that the house is now shrouded in darkness")
        print("confused, you pick yourself up and begin to navigate thought the house")
        print("Soon your eyes adjust to the dark and now you can see")
        print("you around to see where you are and now notice just how oddly the house is designed")
        print("There appears to be two doors to choose from.")
        print("Suddenly the being presents itself before the doors and smiles at you.")
        print(player.getname(), "stands in shock realizing that this is the same being from the visions")
        print("The being states that of these two doors only one will lead to the right path\n")
        print("Available commands: 'points', 'right', 'left', 'help', and 'quit'")
        choice = player.timer(actions, actions_taken)
        print("You chose the right-most door!")
        print("As you open the door the being's smile dissapears and it")
        print("says 'you choose to live again'")
        print("suddenly something from the door pulls you in and everything fades to black.")
        if choice == 'points':
            print("Your current score is:", score)
        elif choice == 'help':
            print("Available commands: 'points', 'right', 'left', and 'quit ")
        elif choice == 'left':
            print("You chose the left-most door!")
            print("The being's smile widens and you begin to sense murderous intent.")
            print("The being says: 'Wrong choice!' and soon the house falls apart.")
            print("You begin to fall into the void..\n")
            print(player.counter_return)
            print("You Died...")            

            exit()
        else:
            choice = player.timer(actions, actions_taken)
        goto(player, score, locations)
        print("You wake up in", locations[7], ".")
        print("You feel weak and groggy and as you awake you see someone sitting down beside your bed")
        print("they look at you and begin to tear up with a smile on their face.")
        print("???: So you're finally awake! i was worried sick its been two whole days!")
        print("As they say this all of your memories suddenly rush back to you and you know what happened.")
        print("You and your best friend were planning on going skiing over winter break")
        print("While at the location you decided to rent a cabin and sleep there for the day then ski tomorrow")
        print("But while you were sleeping a serial killer broke in and tried to kill you.")
        print("your friend managed to get away but the killer's attention was focused on you")
        print("In order to get away you ran and jumped into freezing water so you wouldn't be killed")
        print("the friend called the police and they were able to catch the killer and retrive you from the lake")
        print("however the mix of hypothermia and damage done by jumping in the rocky lake put you in a coma")
        break


# Ending screen with copyright
def end_screen(email_jel, actions_taken):
    print("But then you wonder what was that strange experience you went through and who was that shadowy figure?")
    print("You decide it would be best to think about it later as right now your far too relieved to be alive.")
    print("You finished the game in: ", actions_taken, "Turns!")
    print("Copyright: This game was created by Jelani, and Daniel\n")
    print("If you have any questions feel free to email " + email_jel)
    return(email_jel)


project()
