# Author Jelani
# This program will simulate a text-based game
# Project ver 2

def project():

    fl0 = str("bottom of a tower")
    fl1 = str("first floor")
    fl2 = str("second floor")
    fl3 = str("third floor")
    fl4 = str("Fourth floor")
    fl5 = str("Fith floor")
    final = str("the ground")
    start = title(fl0)
    score = 0
    game_start = game_loop(fl1, score, fl2, fl3, fl4, fl5)
    email_jel = str("jelani.joseph1@marist.edu")
    Ending = end_screen(email_jel, score, final)


# Displays the title screen and Intro 
def title(fl0):
    print("Welcome to Tower_Game\n")
    print("Backstory:\n")
    print("You find yourself at the " + fl0 + ".")
    print("The last thing you can remember is drinking a strange potion, ")
    print("blacking out, and then waking up here. ")
    print("Not knowing what to do you decide to go up the tower.")
    print("You ready yourself for whats to come.\n")
    # add input for player name here
    return(fl0)


# Function to add to score, and show location visited
def change(score, location):
    score = score + 5
    print("Your score is now:", score)
    print("You have passed", location)
    return(score, location)


# Main game loop 
def game_loop(fl1, score, fl2, fl3, fl4, fl5):
    while True:
        print("You start on the " + fl1 + " and see ")
        print("the first defender it seems to be a stone golem. ")
        print("The golem rushes to attack you but you quickly dodge it, ")
        print("you aim your attack at the core, slaying the golem in one blow")
        print("you insert the core from the golem into the slothole ")
        print("the doors slide open and reveal stairs to the next floor")
        location = fl1
        if location == fl1:
            change(score, location)
        print("Going up to " + fl2 + ".\n")
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
        location = fl2
        if location == fl2:
            change(score, location)
        print(" After climbing for some time you reach " + fl3 + ",\n")
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
        print("In your wondering you stumble upon the next ladder")
        location = fl3
        if location == fl3:
            change(score, location)
        print(" You climb up to the ", fl4 + ".")
        print("you realize that the ground is strangely soft.")
        print(" Upon closer inspection you notice that the ground resembles")
        print(" a marsh enviroment, and that there are multiple puddles")
        print(" scatterd all around the floor.")
        print("slowly you walk avoiding the puddles, when suddenly you hear something.")
        print(" It sounded as if something were in the puddles...")
        print("You think carefully about your next actions.")
        print(" Suddenly a large aligator emerges from one of the puddles and moves to another.")
        print(" Terrified, you stand still in awe of the speed and size of the beast.")
        # add a input for the player to make a choice here
        print(" After some time you decide what to do")
        # add an outcome based on input here
        print(" Barely making it out you reach the ladders.")
        location = fl4
        if location == fl4:
            change(score, location)
            print("\n")
        print("Upon reaching ",fl5, ", you take a moment to observe the enviroment")
        print("Looking around you see the area is completely flat and there is only a mirror")
        print("Curious, you contemplate if you look into the mirror ")
        # add input for player to either look at mirror or walk away
        print("Suddenly you hear a shattering noise , the mirror is broken.")
        print("As you survey the area you see that there is another person in the room with you")
        print("You get closer to see who it is, and then you realize that the person looks ")
        print("exactly like you, except they are much paler, and have no pupils")
        print("Suddenly the lookalike stops staring off into space and looks directly ar you")
        print("The strange look-alike rushes the player!")
        # add input for player to either dodge, defend, attack etc.
        print("The lookalike jumps back to recover its footing and begins chanting something")
        print(" You see a large ball of fire growing larger infront of the being.")
        print("It seems like its charging an attack! as the blast approaches you decide to")
        #input for player to: dodge, defend, or attack
        print("The blast is far too large and powerful, the player is caught up in it!")
        print("Soon you feel the pain hit you all at once, its excruciating!")
        print("You see the being rushing toward you, you know its trying to deliver the finishing blow.")
        print(" You cannot dodge, as you are in too much pain to move that fast.")
        # add input for player to: defend, or attack
        print("The force of the being sends you flying through the wall, and you find yourself free falling")
        location = fl5
        if location == fl5:
            change(score, location)
        break
        
# Ending screen with copyright
def end_screen(email_jel, score, final):
    input("Your current location is now in mid-air, as you were sent flying")
    print("You have now reached " + final + " soon you feel a second ")
    print("burst of pain and then everything gets numb as your consciousness fades...\n")
    location = final
    if location == final:
        change(score, location)
    print("You wake up realizing that it was all a dream, yet your body aches all over\n")
    print("Copyright: This game was created by Jelani, and Daniel\n")
    print("If you have any questions feel free to email " + email_jel)
    return(email_jel, score, final)

project()
