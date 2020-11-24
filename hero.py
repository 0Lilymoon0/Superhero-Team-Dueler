import random
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.weapons = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.weapons.append(weapon)

    def attack(self):
        '''Calculate the total damage from all ability attacks. return: total_damage:Int'''
        total_damage = 0
        if len(self.abilities) != 0:
            for ability in self.abilities:
                total_damage += ability.attack()
        if len(self.weapons) != 0:
            for weapon in self.weapons:
                total_damage += weapon.attack()
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
        return int(damage_amt - total_block)

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        self.current_health -= self.defend(damage)

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            return print('Draw')
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                total_damage = self.attack()
                opponent.take_damage(total_damage)
                total_damage2 = opponent.attack()
                self.take_damage(total_damage2)
            if self.is_alive() == False:
                return print(f'{opponent.name} is the winner!')
            elif opponent.is_alive() == False:
                return print(f'{self.name} is the winner!')

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Athena")
    hero2 = Hero("Batman")
    hero3 = Hero("Supergirl")
    team1 = Team("Best_Team")
    team1.add_hero(hero1)
    team1.add_hero(hero2)
    team1.add_hero(hero3)
    team1.view_all_heroes
    team1.remove_hero(hero1)
    team1.view_all_heroes
    team1.remove_hero(hero1)