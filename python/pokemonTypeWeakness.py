#!/usr/bin/env python3
###This is for creatinga  type weakness chart and doing the calculations
###to list all weaknesses and strengths of a combined types of pokemon
###For instance: Water: Weak to Grass, Electric

class TypeWeakness():
    ################################################################################
    def bug(self, attack):
        damage = 1
        if attack == "Fire" or attack == "Flying" or attack == "Rock":
            damage = 2
        elif attack == "Fighting" or attack == "Grass" or attack == "Ground":
            damage = 0.5
               
        return damage
    
    ################################################################################
    def dark(self, attack):
        damage = 1
        if attack == "Bug" or attack == "Fairy" or attack == "Fighting":
            damage = 2
        elif attack == "Dark" or attack == "Ghost":
            damage = 0.5
        elif attack == "Psychic":
            damage = 0
    
        return damage
    
    ################################################################################
    def dragon(self, attack):
        damage = 1
        if attack == "Dragon" or attack == "Fairy" or attack == "Ice":
            damage = 2
        elif attack == "Electric" or attack == "Fire" or attack == "Grass" or attack == "Water":
            damage = 0.5
    
        return damage
    
    ################################################################################
    def electric(self, attack):
        damage = 1
        if attack == "Ground":
            damage = 2
        elif attack == "Electric" or attack == "Flying" or attack == "Steel":
            damage = 0.5
    
        return damage
    
    ################################################################################
    def fairy(self, attack):
        damage = 1
        if attack == "Poison" or attack == "Steel":
            damage = 2
        elif attack == "Bug" or attack == "Dark" or attack == "Fighting":
            damage = 0.5
        elif attack == "Dragon":
            damage = 0

        return damage

    ################################################################################ 
    def fighting(self, attack):
        damage = 1
        if attack == "Fairy" or attack == "Flying" or attack == "Psychic":
            damage = 2
        elif attack == "Bug" or attack == "Dark" or attack == "Rock":
            damage = 0.5
        return damage

    ################################################################################
    def fire(self, attack):
        damage = 1
        if attack in ("Ground", "Rock", "Water"):
            damage = 2
        elif attack in ("Bug","Fairy","Fire","Grass","Ice","Steel"):
            damage = 0.5
        return damage

    ################################################################################ 
    def flying(self, attack):
        damage = 1
        if attack in ("Electric","Ice","Rock"):
            damage = 2
        elif attack in ("Bug","Fighting","Grass"):
            damage = 0.5
        elif attack in ("Ground"):
            damage = 0
        return damage

    ################################################################################
    def ghost(self, attack):
        damage = 1
        if attack in ("Dark","Ghost"):
            damage = 2
        elif attack in ("Bug","Poison"):
            damage = 0.5
        elif attack in ("Fighting","Normal"):
            damage = 0
        return damage

    ################################################################################
    def grass(self, attack):
        damage = 1
        if attack in ("Bug","Fire","Flying","Ice","Poison"):
            damage = 2
        elif attack in ("Electricity","Grass","Ground","Water"):
            damage = 0.5
        return damage

    def ground(self, attack):
        damage = 1
        if attack in ("Grass", "Ice", "Water"):
            damage = 2
        elif attack in ("Poison","Rock"):
            damage = 0.5
        elif attack in ("Electricity"):
            damage = 0
        return damage

    def ice(self, attack):
        damage = 1
        if attack in ("Fighting","Fire","Rock","Steel"):
            damage = 2
        elif attack in ("Ice"):
            damage = 0.5
        return damage

    def normal(self, attack):
        damage = 1
        if attack in ("Fighting"):
            damage = 2
        elif attack in ("Ghost"):
            damage = 0
        return damage

    def poison(self, attack):
        damage = 1
        if attack in ("Ground","Psychic"):
            damage = 2
        elif attack in ("Bug", "Fairy", "Fighting","Grass","Poison"):
            damage = 0.5
        return damage

    def psychic(self, attack):
        damage = 1
        if attack in ("Bug","Dark","Ghost"):
            damage = 2
        elif attack in ("Fighting","Psychic"):
            damage = 0.5
        return damage

    def rock(self, attack):
        damage = 1
        if attack in ("Fighting","Grass","Ground","Steel","Water"):
            damage = 2
        elif attack in ("Fire","Flying","Normal","Poison"):
            damage = 0.5
        return damage

    def steel(self, attack):
        damage = 0.5
        if attack in ("Fighting","Fire","Ground"):
            damage = 2
        elif attack in ("Dark","Electric","Ghost","Water")
            damage = 1
        elif attack in ("Poison"):
            damage = 0
        return damage

    def water(self, attack):
        damage = 1
        if attack in ("Electric","Grass"):
            damage = 2
        elif attack in ("Fire","Ice","Steel","Water"):
            damage = 0.5
        return damage

    def verifyAttackType(self, attack):
        if attack not in ("Bug","Dark","Dragon","Electric","Fairy","Fighting",
                          "Fire","Flying","Ghost","Grass","Ground","Ice",
                          "Normal","Poison","Psychic","Rock","Steel","Water"):
            print("Attack does not match any of the typings.")
            print("Make sure the spelling is correct and the first letter is capitalized.") 
            print("Value given: " + attack)
        return

#weakness = PokemonWeakness()
#print(weakness.verifyAttackType(""))

#print(weakness.fire("Ground") * weakness.water("Ground"))
