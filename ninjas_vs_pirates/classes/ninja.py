import random

class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print (f'{self.name} attacks {pirate.name} with nunchucks! {pirate.name} now has {pirate.health} HP!')
     

    def special_attack(self ,pirate):
        random_num = random.randint(1,3)
        if random_num == 1:
            pirate.health -= self.strength * 2
            print (f'{self.name} throws Ninja Star {pirate.name} takes 20 damage! {pirate.name} now has {pirate.health} HP')
        else: 
            self.strength -= 1
            print(f'{pirate.name} Dodges the ninja star and taunts {self.name}! {self.name} feels defeated and now has {self.strength} strength')

    def level_up(self):
        self.strength += 5
        self.health += 20
        self.speed += 5
        print(f'{self.name} Leveled Up!')
        # Update