# Author Jelani
# This program will simulate a text-based game
# Project ver 2


def project():
    locations = ['forest', 'Cabin', 'Tundra', 'Ocean', 'Cave', 'Tunnel', 'House', 'Ground']
    track_loc = [False, False, False, False, False, False, False, False]
    score = 0
    start = title(locations)
    game_loop(locations, track_loc, start[0:], score)
    email_jel = str("jelani.joseph1@marist.edu")
    Ending = end_screen(email_jel, score, fl5)


# Displays the title screen and Intro
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
    print(" when prompted to input a command type: 'forward' to go forwards")
    print("'right' to turn right, 'left' to go left, and 'think' to think Otherwise")
    print("type 'Help' for help, 'score' to view current score, and 'quit' to exit the game.\n")
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
        elif choice == 'left':
            # left path story
            print("")
        elif choice == 'points':
            score = change(score)
            print("Your current score is: " + score)
        else:
            print("Invalaid command, please refer to the Instructions.\n")
            break
            # add continuation for path here, and score function
        choice = input("Please type an action: ").lower()
        if choice == 'do':
            print("You enhance your body with spirit magic and prepare to dodge ")
            print("After dodging the beast you see an opening to the floor")
            print("not wasting the oppertunity you quickly run to the exit")
        elif choice == 'quit':
            print("exiting game")
            exit()
        elif choice == 'help':
            print("the commands are: 'df' for defend, and, 'at' for attack.")
            print("Otherwise type 'Help' for help, and 'quit' to exit the game.\n")
            choice = input("Please type an action: ").lower()
        elif choice == 'df':
            print("You activate your barrier again except this time")
            print("it is enhanced with spirit energy")
            print("As the banshee touches the pure energy it begins to fade away")
        elif choice == 'at':
            print("This time you decide to call upon shadow magic")
            print("You charge a shadow ball and fire it at the banshee!")
            print("The banshee screams as it crumbles away from the blast")
        else:
            print("Invalaid command, please refer to the Instructions.\n")
            continue
        # Story 
        track_loc[1]
        score
        # Story
        track_loc[2]
        score
        print("you realize that the ground is strangely soft.")
        print(" Upon closer inspection you notice that the ground resembles")
        print(" a marsh enviroment, and that there are multiple puddles")
        print(" scatterd all around the floor.")
        print("slowly you walk avoiding the puddles, when suddenly you hear something.")
        print(" It sounded as if something were in the puddles...")
        print(playername, "thinks carefully about your next actions.")
        print(" Suddenly a large aligator emerges from one of the puddles and moves to another.")
        print(" Terrified, you stand still in awe of the speed and size of the beast.")
        print(" After some time you decide what to do")
        if fl3_visited is True:
            print("Realizing how far you've come you are filled with determination")
            print("You feel a burst of addrenaline, and time seems to slow down for you")
            choice = input("Please type an action: ").lower()
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
        print("Feeling exaughsted you drag yourself to the next staircase.\n")
        track_loc[3]
        score
        print("Looking around you see the area is completely flat and there is only a mirror")
        print("Curious, you contemplate if you look into the mirror ")
        print("you walk toward the mirror and stare at it for some time")
        print("Suddenly you hear a shattering noise , the mirror is broken.")
        print("As you survey the area you see that there is another person in the room with you")
        print("You get closer to see who it is, and then you realize that the person looks ")
        print("exactly like you, except they are much paler, and have no pupils")
        print("Suddenly the lookalike stops staring off into space and looks directly ar you")
        print("The strange look-alike rushes", playername)
        print("frantically you look around for any weapons on the floor since you are depleted of mana")
        print("The lookalike jumps back to recover its footing and begins chanting something")
        print(" You see a large ball of fire growing larger infront of the being.")
        print("It seems like its charging an attack! as the blast approaches you decide to")
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
        print("The blast is far too large and powerful,", playername + " is swallowed up by it!")
        print("Soon you feel the pain hit you all at once, its excruciating!")
        print("You see the being rushing toward you, you know its trying to deliver the finishing blow.")
        print(" You cannot dodge, as you are in too much pain to move that fast.")
        print("The force of the being sends you flying through the wall, and you find yourself free falling\n")
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
