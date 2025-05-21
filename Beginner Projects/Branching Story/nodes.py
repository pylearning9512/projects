#module containing both the nodes of the story in the form of functions, as well as the answers contained in dictionaries

def node0():
    print("You are a scruffy stray dog wandering the streets of a busy neighborhood, your fur is matted, "
          "your stomach growls with hunger, and rain clouds gather overhead. "
          "You spot three different paths ahead:")

    print("  ")
    print("1:follow nose towards delicious smell")
    print("2:investigate the park where children are playing") 
    print("3: head down a quiet residential street with well kept gardens")
    print("  ")

"""first branch"""

def node1():
    print("  ")
    print("you followed your nose towards delicious smell")
    print("")
    print("The restaurant's back alley is filled with wonderful smells. A cook is taking a smoke break by the dumpster. Your stomach rumbles loudly." \
    "  "
    "what will you do?"
          )
    print("  ")
    print("1-wait until they leave")
    print("2-curl up in a cardboard box nearby to rest") 
    print("3- approach the cook with puppy eyes")
    print("  ")
def node1_1():
    print("  ")
    print('You find plenty of half-eaten meals and fill your belly. Suddenly, a van pulls up with "Animal Control" written on the side. Someone must have reported a stray')
          
    print("what will you do?")
    print("  ")
    print("1. Approach the animal control officer with a wagging tail")
    print("2- Run as fast as you can down the alley")
    print("3- Hide deeper in the dumpster")
    print("  ")
def node1_1_1():
    print("  ")
    print("the animal control officer takes you to the shelter, where you spend a couple weeks, nobody comes to adopt you, but you get lucky,")
    print(" one of the shelter workers takes a liking to you and decides to take you home. you are finally safe, and you cant wait to start your new life with your new best friend. ")
    print("  ")

def node1_2():
       print("  ")
       print('The rain begins to fall, but your box stays mostly dry. A young couple taking shelter under an umbrella notices you. "Oh, the poor thing," the woman says.')
       print("  ")
def node1_2_1():
    print("")
    print("")


def node1_3():
    print("  ")
    print('The cook notices you and sighs. "Hungry, huh?" They disappear inside and return with a bowl of scraps. While eating, you hear them on the phone. "Hey, I found a stray dog..."')
    print("  ")    


"""second branch"""

def node1_2():
       print("  ")
       print('The rain begins to fall, but your box stays mostly dry. A young couple taking shelter under an umbrella notices you. "Oh, the poor thing," the woman says.')
       print("  ")
def node1_3():
    print("  ")
    print('The cook notices you and sighs. "Hungry, huh?" They disappear inside and return with a bowl of scraps. While eating, you hear them on the phone. "Hey, I found a stray dog..."')
    print("  ")    


def node2():
    "add node here"


"""
third branch
"""

def node3():
     "add node here"


#answers
choice0={
     1:node1,
     2:node2,
     3:node3
     }

choice1={
    1:node1_1,
    2:node1_2,
    3:node1_3
    }
choice1_1={
    1:node1_1_1,
    }



if __name__ == "__main__":
    print("This module is meant to be imported, not run directly.")
