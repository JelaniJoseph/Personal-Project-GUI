# Author Jelani
# This program will simulate a text-based game
# Project ver 1

def project():

    fl0 = str("bottom of a tower")
    fl1 = str("first floor")
    fl2 = str("second floor")
    fl3 = str("third floor")
    fl4 = str("Fourth floor")
    fl5 = str("Fith floor")
    fl6 = str("Sixth floor")
    final = str("the ground")
    start = title(fl0)
    score = 0
    game_start = game_loop(fl1, score, fl2, fl3, fl4, fl5, fl6)
    email_jel = str("jelani.joseph1@marist.edu")
    Ending = end_screen(email_jel, fl3, final)


# Displays the title screen and Intro 
def title(fl0):
    print("Welcome to Tower_Game\n")
    print("Backstory:\n")
    print("You find yourself at the " + fl0 + ".")
    print("The last thing you can remember is drinking a strange potion, ")
    print("blacking out, and then waking up here. ")
    print("Not knowing what to do you decide to go up the tower.")
    print("You ready yourself for whats to come.\n")
    return(fl0)


def change(score, location):
    score = 0
    score +=  5
    print("Your score is now:", score)
    print("Your position is now:", location)
    return(score, location)

def game_loop(fl1, score, fl2, fl3, fl4, fl5, fl6):
    while True:
        print("You start on the " + fl1 + " and see ")
        print("the first defender it seems to be a stone golem. ")
        print("The golem rushes to attack you but you quickly dodge it, ")
        print("you aim your attack at the core, slaying the golem in one blow")
        print("you insert the core from the golem into the slothole ")
        print("the doors slide open and reveal stairs to the next floor")
        location = fl1
        if location == fl1:
            print("You have passed ", fl1)
        change(score, location)
        print("Going up to " + fl2 + ".\n")
        print("You wait for a while staring at the staircase, ")
        print("catching your breath after the sudden burst of addrenaline")
        print("After a while you calm yourself practicing breathing techniques ")
        print("and will yourself to walk up to the next level ")
        print("Upon reaching the " + fl2 + "you look ")
        print("around and notice that the field is strangely empty and very dark.")
        print(" observing the enviroment, slowly walking ")
        print("around the floor suddenly a ear-piercing cry is heard")
        print("You turn around to see a Banshee of sorts, ")
        print("it is pitch black and see-through the beast has long sharp claws")
        print("and an unhinged jaw filled with sharp rows of teeth, ")
        print("the creature turns to you and its eyes turn red")
        print("You begin to feel uneasy as you know the battle is about to begin")
        print("The beast charges at you with full speed, ")
        print("you barely manage to dodge it getting scratched while doing so")
        print(" After recieving the damage you take into consideration ")
        print("how poor your defenses are so you cast a barrier. ")
        print("The beast circles back and attacks the barrier but ")
        print("it cannot break through it, during the chaos of its relentless attacks")
        print("you begin to charge your fireball attack ")
        print("and line it up so that it will hit the creature")
        print("The creature, mindlessly still attacking, ")
        print("does not even move at the notice of the blast and is incenerated. ")
        print("While the beat is being engulfed in flames ")
        print("you notice another item being dropped, its a bone key.")
        print(" Already knowing what to do you grasp the bone key, ")
        print("insert it in the keywhole further down and unlock the next area.")
        print(" This time it is a set of ladders.\n")
        print(" After climbing for some time you reach " + fl3 + ",")
        print(" and notice how foggy and blocked the area seems\n")
        change(score, location)
        input("Your current location is now " + fl3 + " Press Enter to continue...\n")
        print(" After looking around you find the area ")
        print("looks almost maze-like... in fact it is a maze!")
        print(" you begin to walk through the entrance of the maze ")
        print("and after a few hours of traversing you find yourself lost.")
        print(" while going through you feel as if something else is in the maze with you... ")
        print("then you suddenly hear footsteps and heavy breathing ")
        print(" From the side of your eye you notice a ")
        print("large black mass approaching you at high speeds!")
        print(" In a bout of pure fear you run as fast as you can away from the approaching mass. ")
        print(" Going in a straight line you begin to see a light, ")
        print("it must be the exit! you quicken yourself with enhancement magic")
        print(" Leaping with all your might you manage to ")
        print("pass through the door right as the mass crashes into it behind you")
        print(" As you fly through the blinding light ")
        print("you realize that there is no floor...")
        print("In realizing this you look around trying to ")
        print("find a ledge to catch so you wont plummit and die.")
        print(" However nothing shows, and you are far ")
        print("too exaughsted to use magic for a lighter fall")
        print("Seconds feels like hours as you recall your past memories, ")
        print("you know that this is the end.\n")
        change(score, location)
        break


def end_screen(email_jel, fl3, final):
    input("Your current location is now in mid-air, as you just lept from the " + fl3 + ".")
    print("You have now reached " + final + " soon you feel a ")
    print("burst of pain and then everything gets numb as your consciousness fades...\n")
    change(score, location)
    input("Your Final score was:" + " " + str(score) + " ,It seems this is the end...\n")
    if score == (15):
        print("You Died...\n")
    print("Copyright: This game was created by Jelani, and Daniel\n")
    print("If you have any questions feel free to email " + email_jel)
    return(email_jel)

project()
