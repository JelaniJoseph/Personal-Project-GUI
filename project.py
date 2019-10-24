# Author Jelani
# This program will simulate a text-based game
# Project ver 2

def project():

    fl0 = str("bottom of a tower")
    fl1 = str("first floor")
    fl2 = str("second floor")
    fl3 = str("third floor")
    fl4 = str("Fourth floor")
    fl5 = str("Last floor")
    fl0_visited = False
    fl1_visited = False
    fl2_visited = False
    fl3_visited = False
    fl4_visited = False
    fl5_visited = False
    final_visited = False
    score = 0
    start = title(fl0)
    game_start = game_loop(fl0, fl1, score, fl2, fl3, fl4, fl5, start[1])
    email_jel = str("jelani.joseph1@marist.edu")
    Ending = end_screen(email_jel, score, fl5)


# Displays the title screen and Intro 
def title(fl0):
    print("Welcome to Tower_Game")
    print("=========================\n")
    playername = input("Enter a username here: ")
    print("Backstory:\n")
    print("You find yourself at the " + fl0 + ".")
    print("The last thing you can remember is drinking a strange potion, ")
    print("blacking out, and then waking up here. ")
    print("Not knowing what to do you decide to go up the tower.")
    print("You ready yourself for whats to come.\n")
    print("Instructions:\n")
    print(" when prompted to input a command type: 'do' for dodge "
    "'df' for defend, and 'at' for attack. Otherwise type 'Help' for help, and 'quit' to exit the game.\n")
    print("Otherwise, have fun! and thanks for playing Tower_Game!")
    input("Press Enter to Start")
    fl0_visited = True
    # add input for player name here
    return(fl0, playername)


# Function to add to score, and show location visited
def change(score, location):
    score +=5
    my_list = ['Second Floor', 'Second Floor', 'Third Floor','Fourth floor', 'Last Floor', 'The Ground']
     
    print("Your score is now:", str(score))
    print("You have passed", location)
    print("Going up to the", my_list[score // 5], "\n")
    return(score, location)


# Main game loop, when you see player take it out for the variable
def game_loop(fl0, fl1, score, fl2, fl3, fl4, fl5, playername):

    while True:
        
        print("You start on the " + fl1 + " and see ")
        print("the first defender it seems to be a stone golem. ")
        print("The golem rushes to attack you but you quickly ")
        choice = input("Please type an action: ").lower()
        if choice == 'do':
            print("You dodge the golem, and it crumbles from its own might ")
        elif choice == 'df':
            print("You activate your barrier as the golem punches, ")
            print("The beast falls backwards and crumbles away")
        elif choice == 'at':
            print("You quickly charge a fireball and blast the beast")
        elif choice == 'quit':
            print("exiting game")
            exit()
        elif choice == 'help':
            print("the commands are: 'df' for defend, and, 'at' for attack.")
            print("Otherwise type 'Help' for help, and 'quit' to exit the game.")
            continue
        else:
            print("Invalaid command, please refer to the Instructions.\n")
            continue

        print("a core drops from the golem's chest and it collapses.")
        print("you insert the core from the golem into the slothole ")
        print("the doors slide open and reveal stairs to the next floor\n")
        location = fl1
        if location == fl1:
            fl1_visited = True
            score, location = change(score, location)
        print("You wait for a while staring at the staircase, ")
        print("catching your breath after the sudden burst of addrenaline")
        print("After a while you calm yourself practicing breathing techniques ")
        print("and will yourself to walk up to the next level ")
        print("Upon reaching the", fl2 + "you look ")
        print("around and notice that the field is strangely empty and very dark.")
        print(" observing the enviroment, slowly walking ")
        print("around the floor suddenly a ear-piercing cry is heard")
        print("You turn around to see a Banshee of sorts, ")
        print("it is pitch black and see-through the beast has long sharp claws")
        print("and an unhinged jaw filled with sharp rows of teeth, ")
        print("the creature turns to you and its eyes turn red")
        print("You begin to feel uneasy as you know the battle is about to begin")
        print("The beast charges at you with full speed, ")
        choice = input("Please type an action: ").lower()
        if choice == 'do':
            print("You dodge the banshee but as it passes you it suddenly dissapears ")
            
        elif choice == 'df':
            print("You activate your barrier as the banshee approaches ")
            print("The banshee phases through it and screams inside the barrier")
        elif choice == 'quit':
            print("exiting game")
            exit()
        elif choice == 'help':
            print("the commands are: 'df' for defend, and, 'at' for attack.")
            print("Otherwise type 'Help' for help, and 'quit' to exit the game.") 
        elif choice == 'at':
            print("You charge a fireball and blast it toward the banshee")
            print("But it was not strong enough! the beast flys right through it ")
        else:
            print("Invalaid command, please refer to the Instructions.\n")
            continue
        
        print("shocked from what just happened you freeze, wondering what to do next")
        print(" While in shock, the banshee scratches you, and an icey sharp pain is felt. ")
        print("regaining your senses you quickly dart back getting out of range.")
        print("the banshee turns around quickly, it seems angry...")
        print("you think of what to do next")
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
            print("Otherwise type 'Help' for help, and 'quit' to exit the game.") 
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
               
        print("After you exit the door for the stairs, the door behind you closes.")
        print("You take a moment to catch your breath, and begin heading toward")
        print(" the stairs to the next floor.\n")
        location = fl2
        if location == fl2:
            fl2_visited = True
            score, location = change(score, location)
        print(" and notice how foggy and blocked the area seems")
        print(" After looking around you find the area ")
        print("looks almost maze-like... in fact it is a maze!")
        print(" you begin to walk through the entrance of the maze ")
        print("and after a few hours of traversing you find yourself lost.")
        print(" while going through you feel as if something else is in the maze with you... ")
        print("then you suddenly hear footsteps and heavy breathing ")
        print(" From the side of your eye you notice a ")
        print("large black mass approaching you at high speeds!")
        print("You quickly deicide which path to take to avoid it.")
        print(" Choosing path on the right, you manage to escape the beast. ")
        print("You take a moment to calm down, and catch your breath.")
        print(" Soon you get back up and continue through the maze")
        print("In your wondering you stumble upon the next ladder\n")
        location = fl3
        if location == fl3:
            fl3_visited = True
            score, location = change(score, location)
        print("you realize that the ground is strangely soft.")
        print(" Upon closer inspection you notice that the ground resembles")
        print(" a marsh enviroment, and that there are multiple puddles")
        print(" scatterd all around the floor.")
        print("slowly you walk avoiding the puddles, when suddenly you hear something.")
        print(" It sounded as if something were in the puddles...")
        print(playername,"thinks carefully about your next actions.")
        print(" Suddenly a large aligator emerges from one of the puddles and moves to another.")
        print(" Terrified, you stand still in awe of the speed and size of the beast.")
        print(" After some time you decide what to do")
        if fl3_visited == True:
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
        location = fl4
        if location == fl4:
            fl4_visited = True
            score, location = change(score, location)
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
        if fl4_visited == True:
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
                continue
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
        location = fl5
        if location == fl5:
            fl_5visited = True
            score, location = change(score, location)
        break


# Ending screen with copyright
def end_screen(email_jel, score, fl5):
    print("Your current location is now in mid-air, as you were sent flying")
    print("You have now reached "  " soon you feel a second ")
    print("burst of pain and then everything gets numb as your consciousness fades...\n")
    if fl5_visited == True:
        print("You reflect on your journey as you plumit whilst on fire...")
    print("You wake up realizing that it was all a dream, yet your body aches all over\n")
    print("Copyright: This game was created by Jelani, and Daniel\n")
    print("If you have any questions feel free to email " + email_jel)
    return(email_jel, score, fl5)

project()
