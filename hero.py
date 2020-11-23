import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks. return: total_damage:Int'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return int(total_damage)

    def add_armor(self, armor):
        '''Add armor to self.armors. Armor: Armor Object'''
        self.armors.append(armor)

    def defend(self, damage_amt):
        '''Calculate the total block amount from all armor blocks. return: total_block:Int'''
        total_block = 0
        if len(self.armors) != 0:
            for armor in self.armors:
                total_block += armor.block()
                total_block -= damage_amt
        else:
            total_block -= damage_amt
        return int(total_block)

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        self.current_health -= (damage + self.defend(damage))

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won
        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
        # 3) After each attack, check if either the hero (self) or the opponent is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
        if len(hero1.abilities) == 0 and len(opponent.abilities) == 0:
            return print('Draw')
        else:
            while hero1.is_alive() == True and opponent.is_alive() == True:
                total_damage = hero1.attack()
                opponent.take_damage(total_damage)
                opponent.is_alive()
                total_damage2 = opponent.attack()
                hero1.take_damage(total_damage2)
                hero1.is_alive()
            if hero1.is_alive() == False:
                return print(f'{opponent.name} is the winner!')
            elif opponent.is_alive() == False:
                return print(f'{hero1.name} is the winner!')

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    armor1 = Armor("Wizard Cloak", 900)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero2.add_armor(armor1)
    hero1.fight(hero2)