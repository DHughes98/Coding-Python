import random

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print(f'{self.name} attacks {ninja.name} with Cutlass! {ninja.name} now has {ninja.health} HP!')
        

    def special_attack (self , ninja):
        random_num = random.randint(1,10)
        if random_num == 5:
            ninja.health -= self.strength * 7
            print (f'{self.name} Fires the BoomStick {ninja.name} explodes into smithereens')
        elif random_num == 1:
            self.health -= self.strength * 10
            print(f'The Boomstick has backfired {self.name} explodes into smithereens')
        else:
            print(f'{ninja.name} dodges the cannonball and taunts {self.name}! {self.name} feels defeated and now has {self.strength} strength.')
            self.strength -= 1.5


