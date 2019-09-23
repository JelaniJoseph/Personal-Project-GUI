# Author Jelani
# This program will simulate a text-based game


def project():

    fl1 = str("first floor")
    fl2 = str("second floor")
    fl3 = str("third floor")
    death = str("the ground")
    score = 0
    print("Welcome to Tower_Game\n")
    print("Backstory:\n")
    print("You find yourself at the bottom of a large spiraling tower")
    print("After a long journey and many fights you have finally located the bast of operations")
    print("However the only way to reach the boss you must progress through four different floors each with a guardian")
    print("So let's see if your prepared for the task!\n")
    print("You start on the " + fl1 + " and see the first guardian it seems to be a stone golem")
    print("The golem rushes to attack you but you quickly dodge it, and aim your attack at the core, slaying the golem in one blow")
    print("you insert the core from the golem into the slothole the doors slide open and reveal stairs to the next floor")
    input("Press Enter to view your score, and location\n")
    score = score + 5
    input("Your score is now:" + str(score) + " ,and you are currently at the " + fl1 + ".")
    input("Press Enter to continue:\n ")
    print("You wait for a while staring at the staircase, catching your breath after the sudden burst of addrenaline")
    print("After a while you calm yourself practicing breathing techniques and will yourself to walk up to the next level")
    print("Upon reaching the " + fl2 + "you look around and notice that the field is strangely empty and very dark")
    print("observing the enviroment, slowly walking around the floor suddenly a ear-piercing cry is heard")
    print("You turn around to see a Banshee of sorts, it is pitch black and see-through the beast has long sharp claws")
    print("and an unhinged jaw filled with sharp rows of teeth, the creature turns to you and its eyes turn red")
    print("You begin to feel uneasy as you know the battle is about to begin")
    print("The beast charges at you with full speed, you barely manage to dodge it getting scratched while doing so")
    print(" After recieving the damage you take into consideration how poor your defenses are so you cast a barrier. ")
    print("The beast circles back and attacks the barrier but it cannot break through it, during the chaos of its relentless attacks")
    print("you begin to charge your fireball attack and line it up so that it will hit the creature")
    print("The creature, mindlessly still attacking, does not even move at the notice of the blast and is incenerated. ")
    print("While the beat is being engulfed in flames you notice another item being dropped, its a bone key.")
    print(" Already knowing what to do you grasp the bone key, insert it in the keywhole further down and unlock the next area.")
    print("This time it is a set of ladders.\n")
    input("Press Enter to view your score, and location\n")
    score = score + 5
    input("Your score is now:" + str(score) + " ,and you are currently at the " + fl2 + ".")
    input("Press Enter to continue...\n")
    print(" After climbing for some time you reach " + fl3 + ", and notice how foggy and blocked the area seems\n")
    input("Your current location is now " + fl3 + " Press Enter to continue...\n")
    print(" After looking around you find the area looks almost maze-like... in fact it is a maze!")
    print(" you begin to walk through the entrance of the maze and after a few hours of traversing you find yourself lost")
    print(" while going through you feel as if something else is in the maze with you... then you suddenly hear footsteps and heavy breathing")
    print(" From the side of your eye you notice a large black mass approaching you at high speeds ")
    print(" In a bout of pure fear you run as fast as you can away from the approaching mass. ")
    print(" Going in a straight line you begin to see a light, it must be the exit! you quicken yourself with enhancement magic")
    print(" Leaping with all your might you manage to pass through the door right as the mass crashes into it behind you")
    print(" As you fly through the blinding light you realize that there is no floor...")
    print("In realizing this you look around trying to find a ledge to catch so you wont plummit and die")
    print("However nothing shows, and you are far too exaughsted to use magic for a lighter fall ")
    print("Seconds feels like hours as you recall your past memories, you know that this is the end.\n")
    input("Your current location is now in mid-air, as you just lept from the " + fl3 + ".")
    print("You have now reached " + death + " soon you feel a burst of pain and then everything gets numb as your consciousness fades...\n" )
    score = score + 5
    input("Your Final score was:" + str(score) + " ,It seems this is the end...\n")
    if score == (15):
        print("You Died...")

project()

