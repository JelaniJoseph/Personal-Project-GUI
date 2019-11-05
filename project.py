# Author Jelani
# This program will simulate a text-based game
# Project ver 2


def project():
    locations = ['forest', 'Cabin', 'Tundra', 'Ocean', 'Cave', 'Tunnel', 'House', 'Ground']
    track_loc = [True, True, True, True, True, True, True, True]
    score = 0
    start = title(locations)
    game_loop(locations, track_loc, start[0:], score)
    email_jel = str("jelani.joseph1@marist.edu")
    Ending = end_screen(email_jel, score, fl5)


# Displays the title screen and Intro
# Allows player to choose username
def title(locations):
    print("Welcome to Bio-Saga")
    print("=========================\n")
    print("Backstory:\n")
    print("You find yourself inside a", locations[0])
    print("Your head hurts, and you cant remember how you got here.")
    print("You try and remember your name... it was something like..")
    playername = input("Enter a username here: ")
    print("You look around and see that you are surrounded by strange trees.")
    print("Not knowing what else to do or where to go you get up and begin to wander.")
    print("Soon you find a sort of entrance in the forest, you decide to walk in.\n")
    print("Instructions:\n")
    print("Be sure to read carefully, as the list of available commands will be shown to the user.")
    print("type 'Help' to view the commands, 'score' to view current score, and 'quit' to exit the game.\n")
    print("Otherwise, have fun! and thanks for playing Bio-Saga!")
    input("Press Enter to Start")
    return(playername)


# Function to add to score, and show location visited
def change(score):
    score+=5
    return(score)


# Main game loop, when you see player take it out for the variable
def game_loop(locations, track_loc, playername, score):
    while True:
        print("As you enter the strange", locations[0], "you feel as if your being watched....")
        print("cold, and confused you continue trying to find some clues as to where you are.")
        print("As you walk you come across a winding path with three possible paths.\n")
        print("How will you advance?")
        choice = input("Please type an action: ").lower()
        if choice == 'forward':
            print("You decide to keep walking forward. ")
        elif choice == 'left':
            print("You decide to take the left path, and begin to walk. ")
        elif choice == 'right':
            print("You decide to take the right path, and begin to walk. ")
        elif choice == 'quit':
            print("exiting game")
            exit()
        elif choice == 'help':
            print("the commands are: 'forward', 'right', 'left'")
            print("Otherwise type 'Help' for help, and 'quit' to exit the game.\n")
            choice = input("Please type an action: ").lower()
        else:
            print("Invalaid command, please refer to the Instructions.\n")
            continue
        print("you soon arrive at  another area of the forest, the trees somehow seem more sinister")
        print("You start to notice that the forest has gone completely silent,")
        print("a low roar can be heard in the distance, it would be best to consider which ")
        print("path you choose from now on...\n")
        track_loc[0]
        score = change(score)
        print("While walking you begin to wonder why it is you cant remember anything")
        print("the last thing you can remember was waking up in this forest in pain")
        print("You stop moving, and begin to try thinking about the situation and how")
        print(" you plan to find out about your past")
        print("Suddenly, the low roaring sound begins to pick up")
        print("whatever is making that noise seems to be approaching you at an alarming rate")
        print(playername,"decides it would be best to continue as fast as possible")
        print(" as", playername, "starts to jog they come across another split passage")
        print("This time the passage only has two routes, forward or right.")
       # in choices have options that end game and return score
        choice = input("Which way will you go?: ").lower()
        if choice == 'forward':
            # forward story
            print("")
        elif choice == 'right':
            # right path story
            print("")
        elif choice == 'quit':
            print("exiting game")
            exit()
        elif choice == 'help':
            print("the commands are: 'df' for defend, and, 'at' for attack.")
            print("Otherwise type 'Help' for help, and 'quit' to exit the game.")
            choice = input("Please type an action: ").lower()
        elif choice == 'points':
            print("Current Score: ", score)
            print("Your current score is: " + score)
        else:
            print("Invalaid command, please refer to the Instructions.\n")
            break
            print("As you walk along the path with a hastened pace you see something in the distance")
            print("You squint and can barely make out the figure of a log cabin")
            print("while you gaze at the log cabin a roar heard in the distance catches your attention")
            print("Whatever it is thats approaching its even close than before you decide to hide out in the cabin")
            print(playername, "leaves now enters the", locations[1], ".\n")
            track_loc[1]
            score = change(score)
            print("As you enter", locations[1], "you feel slightly safer")
            print("You decide that now is a good time to think about the situation")
            print("While your lost in deep thought trying to remember anything you have a vision")
            print("In this vision you see a strange being entering the cabin wearing winter gear, exaughsted.")
            print("As you take of your winter gear in this vision you see the being pull up a chair and sit down")
            print("The being then opens up a drawer next to the table and pulls out a large peice of paper")
            print("Suddenly the vision is intereupted by the sound of something hitting the cabin")
            print("remembering the vision you decide it would be best to inspect the drawer")
            print("You open the drawer next to the table and see something insde, its just like in the vision.")
            print("You open the paper, and soon realize that its a map of the area!")
            print("Remember, when you want to look at the map simply type in 'map' to see where you are")
            print("After getting the map you decide it would be best to keep it on you and head out")
            print("You get up and head to the backdoor, you open it expecting to see the forest again")
            print("Except that its no longer a forest, its actually now a", locations[2])
            print("Freezing, and confused you try and look at your surrounding area to see where to go")
            print("You see that your only  way to go is either forward, or check the map")
            print("Afterall theres no point in wandering aimlesly!\n")
            track_loc[2]
            score = change(score)
        choice = input(playername,"decides that they will: ").lower()
        if choice == 'forward':
            print("you decide to go straight ahead unknowing the dangers that lie ahead!")
            print(" as you start to trudge on you begin to suffer from frostbite ")
            print("Freezing, you start to shake and desperately desire shelter")
            print("You head back to",locations[2], "in order to warm back up")
            print("You decide it would probably be best to look at the map before heading out.")
        elif choice == 'quit':
            print("exiting game")
            exit()
        elif choice == 'points':
            print("Current score: ", score)
        elif choice == 'help':
            print("the commands are: 'df' for defend, and, 'at' for attack.")
            print("Otherwise type 'Help' for help, and 'quit' to exit the game.\n")
            choice = input("Please type an action: ").lower()
        elif choice == 'map':
            # display the map to the player
            print("You see that the best path to take and memorize it")
            print("before you leave you remember the winter gear from the past vision")
            print("after scavenging around for a few minuets you find the gear and equip it")
            print(playername,"walks out of the house and begins to follow the path.")
        else:
            print("Invalaid command, please refer to the Instructions.\n")
            continue
        print("After following the path you soon find yourself infront of a large", locations[3])
        print("You skeptically look at the water and suddenly while looking at your reflection you remember something.")
        print("You see another vision but this time the being is jumping into the freezing water and swiming down to")
        print("what seems to be a cave about twenty feet in the water.")
        print("you snap out of the vision and think that theres no way your going to jump into the")
        print("freezing water, youll surely get hypothermia.")
        print("you turn around to go back to the cabin when you feel a presence next to you")
        print("it seems to be a hulking white beast standing on two legs with horns")
        print("while staring at the beast you device a plan, it would be best to either dive in.")
        print("the beings yellow eyes look down upon you and it starts to drool, you must act quickly!\n")
        # add a time limit to below functions
        score = change(score)
        print("With your burst of adrenaline you swim as fast as you can downards like you saw in the vision")
        print("While swimming you feel as if a presence is coming after you, you quicken your pace")
        print("Soon you enter the", locations[4], "and the entrance seals, whatever behind it also being blocked off")
        print("the water dissapears from within it and you can breathe")
        print("you pick yourself up and shed your wintergear, as the cave is odly humid and warm")
        print("you look around and notice a wierd pattern on the wall")
        print("it seems to show arrows pointing in various directions")
        print("it reads: forward, left, right")
        print("you decide it would be best to memorize this pattern.")
        print("As you advance you come across three pathways, it seems you must choose one to go on.")
        track_loc[4]
        score

        choice = input("What will",playername, "do?: ").lower()
        if choice == 'do':
            print("You dodge the creature, after enhancing yourself it charges past you, and through a wall")
            print("It bursts through the wall and falls to its death.")
        elif choice == 'quit':
            print("exiting game")
            exit()
        elif choice == 'help':
            print("the commands are: 'df' for defend, and, 'at' for attack.")
            print("Otherwise type 'Help' for help, and 'quit' to exit the game.")
            choice = input("Please type an action: ").lower()
        elif choice == 'df':
            print("You cast a strong barrier as the beast charges")
            print("It slams its head against the barrier but it is too dense to be broken")
            print("The beast shatters it skull against your barrier and dies")
        elif choice == 'at':
            print("You charge a fire blast and fire away at the beast!")
            print("you seem to hit a vital spot and the beast looses control of its direction")
            print("The beast falls down and bleeds out, it wont be moving anytime soon.")
        else:
            print("Invalaid command, please refer to the Instructions.\n")
            continue
        
        track_loc[3]
        score
        
        choice = input("Please type an action: ").lower()
        if choice == 'do':
            print("You dodge the creature, after enhancing yourself it charges past you, and through a wall")
            print("It bursts through the wall and falls to its death.")
        elif choice == 'df':
            print("You cast a strong barrier as the beast charges")
            print("It slams its head against the barrier but it is too dense to be broken")
            print("The beast shatters it skull against your barrier and dies")
        elif choice == 'at':
            print("You charge a fire blast and fire away at the beast!")
            print("you seem to hit a vital spot and the beast looses control of its direction")
            print("The beast falls down and bleeds out, it wont be moving anytime soon.")
        elif choice == 'help':
            print("the commands are: 'df' for defend, and, 'at' for attack.")
            print("Otherwise type 'Help' for help, and 'quit' to exit the game.")
            choice = input("Please type an action: ").lower()
        elif choice == 'quit':
            print("exiting game")
            exit()
        else:
            print("Invalaid command, please refer to the Instructions.\n")
            continue
        
        track_loc[4]
        score
        #story
        #paths + score return
        track_loc[5]
        score
        # Story
        # Paths and score return
        track_loc[6]
        score
        # Story
        # Paths and score return
        track_loc[7]
        score
        # ending part of story
        # Paths and score return
        # at end have it lead up to endscreen
        break


# Ending screen with copyright
def end_screen(email_jel, score, fl5,):
    # add story for ending involve it with waking up from brink of death
    # add hearing a voice at end of the tunnel and leave a cliff hanger
    location = fl5
    if location == fl5:
        print("You reflect on your journey as you plumit whilst on fire...")
        print("You wake up realizing that it was all a dream, yet your body aches all over\n")
        print("Copyright: This game was created by Jelani, and Daniel\n")
        print("If you have any questions feel free to email " + email_jel)
    return(email_jel, score, fl5)


project()
