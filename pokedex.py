#!/usr/bin/env python3


### Purpose of this class is to read from a csv file
### a list of all the pokemon that exists in the current gen
### and create a curated list of pokemon ideal for tera raids
### based on the calculations made with pokemonDualWeakness.py

import csv
import pokemonDualWeakness

class Pokedex:
    
    damageDict = {1: [1,1], 2:[1,.5],3:[1,.25],4:[1,0],5:[.5,.5],6:[.5,.25],7:[.5,0],8:[.25,.25],9:[.25,0],10:[0,0]}
    number = 0
    name = 1
    type1 = 2
    type2 = 3
    hp = 4
    attack = 5
    defense = 6
    spAttack = 7
    spDefense = 8
    speed = 9
    combinedStats = 10

    def pokemonList(self,pkType,pkList,combinedStats=0):
        # Need to create a csv reader to read from csv file 
        # a list of pokemon that match the output from pokemonTypeWeakness
        pokemonList = []
        for types in pkType:
            type1 = types.split("/")[0]
            try:
                type2 = types.split("/")[1]
            except:
                type2 = ""
            for pokemon in range(len(pkList)-1):
                if (type1 == pkList[pokemon+1][self.type1] and type2 == pkList[pokemon+1][self.type2]):
                    if (int(pkList[pokemon+1][self.combinedStats])>=combinedStats):
                        pokemonList.append(pkList[pokemon+1])
        #for i in pokemonList:
        #    print (i)
        return pokemonList

    def findHighestDamageResistantPokemon(self, pokemon,teraType, pokemonList,combinedStats=0):
        #Iterate through all options of damage till you find a pokemon that
        #matches the type most effective at dealing damage and takes the least possible amount
        matchup = pokemonDualWeakness.DualType()
        mostResistant = [] 
        damage = 10
        count =  0
        while damage >= 1:
            teraTypeCounter = matchup.teraTypeCounter(pokemon,teraType,self.damageDict[damage])
            if len(teraTypeCounter)>1:
                avoidTera = matchup.avoidTeraType(teraTypeCounter,teraType,self.damageDict[damage])
                if len(avoidTera)>1:
                    mostResistant.append(avoidTera)
                    if len(mostResistant[count]) > 1:
                        suggestion = self.pokemonList(mostResistant[count],pokemonList,combinedStats)
                        count +=1
                        if len(suggestion)>1:
                            print("Level of resistance: ", self.damageDict[damage])
                            return suggestion
            damage -= 1

    def findPokemon(self, name, pkList):
        #Looks for pokemon and returns Pokemon name, type(s), and stats
        pokemon = ""
        for i in range(len(pkList)-1):
            if name == pkList[i+1][1]:
                pokemon = pkList[i+1]
        return pokemon
        
    def csvReader(self):
        #Reads through csv file to get relevant data
        pokemon = []
        with open("pokedex.csv", 'r') as file:
            reader = csv.reader(file,skipinitialspace=True,delimiter=",")
            for row in reader:
                pokemon.append(row)
        return pokemon

def main():
    pokedex = Pokedex()
    matchup = pokemonDualWeakness.DualType()
    pokemonList = pokedex.csvReader()
    while(True):
        print("Enter q to quit or r to reset")
        pkmon = input("Enter pokemon: ").lower().capitalize()
        if pkmon == "Q":
            break
        elif pkmon == "R":
            continue
        teraType = input("Enter tera type: ").lower().capitalize()
        if teraType == "Q":
            break
        elif teraType == "R":
            continue
        pokemon = pokedex.findPokemon(pkmon,pokemonList)
        #typeMatchups = matchup.teraTypeCounter(pokemon,teraType,pokedex.damageDict[2])
        #print("Type matchups")
        #for i in typeMatchups:
        #    print(i)
        #avoidTera = matchup.avoidTeraType(typeMatchups,teraType,pokedex.damageDict[2])
        #print("avoid tera matchups")
        #for i in avoidTera:
        #    print(i)
        suggestion = pokedex.findHighestDamageResistantPokemon(pokemon,teraType,pokemonList,400)
        #suggestion = pokedex.pokemonList(avoidTera,pokemonList,420)
        for i in suggestion:
            print(i)


if __name__ == "__main__":
    main()
