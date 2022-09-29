
from classes.ninja import Ninja
from classes.pirate import Pirate
import random



michelangelo = Ninja("Michelangelo")

jack_sparrow = Pirate("Jack Sparrow")

print("Welcome to Ninjas VS Pirates")

while(michelangelo.health > 0 and jack_sparrow.health > 0):
    response = ""
    while not response == "1" and not response == "2":
        print("You are Michelangelo, will you \n 1) Attack \n 2) Special Attack")
        response = input(">>>")
        if response == "1":
            michelangelo.attack(jack_sparrow)
        else: 
            response == "2"
            michelangelo.special_attack(jack_sparrow)
        
        Jack_action = random.randint(1,2)
        if Jack_action == 1:
            jack_sparrow.attack(michelangelo)
        else:
            jack_sparrow.special_attack(michelangelo)
        
        if michelangelo.health <= 0:
            print(f"{michelangelo.name} has to walk the plank!")
        if jack_sparrow.health <= 0:
            print(f"{jack_sparrow.name} has to commit seppuku")


print("Level Complete!")















