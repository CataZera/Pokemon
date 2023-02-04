#!/usr/bin/env python3
###Class is for a list of defined dual type weaknesses against singular types and other dual types

import sys
import pokemonTypeWeakness
import pdb
class DualType(object):

    typesList = ["Normal","Fire","Water","Electric","Grass","Ice",
                 "Fighting","Poison","Ground","Flying","Psychic","Bug",
                 "Rock","Ghost","Dragon","Dark","Steel","Fairy"]

    debug = False

    def dualTypeWeakness(self,type1,type2):
        #Returns a list of damage that type1 + type2 can receive from all 18 typings
        types = pokemonTypeWeakness.TypeWeakness()
        t1 = getattr(types,type1.lower())
        if type2 != "":
            t2 = getattr(types,type2.lower())
        typeList = []
        damageList = []
        for i in self.typesList:
            if(type2 ==""):
                damageList.append(i)
                damageList.append(t1(i))
            else:
                damageList.append(i)
                damageList.append(t1(i)*t2(i))
        if(self.debug):
            print(type1 + "/" + type2 + " weaknesses")
            for i in range(len(damageList)-1):
                if type(damageList[i]) == str:
                    print(damageList[i], damageList[i+1]) 
        return damageList

    def monoTypeSuperEffective(self,type1):
        #Everything type1 is weak against, gets hit with super effective attacks
        types = pokemonTypeWeakness.TypeWeakness()
        typeList = []
        t1 = getattr(types,type1.lower())
        for i in self.typesList:
            if (t1(i)>1 and i not in typeList):
                typeList.append(i)
            for j in self.typesList:
                dualType = i+"/"+j
                if((t1(j)>1 or t1(i)>1) and dualType not in typeList and i != j):
                    typeList.append(dualType)
        return typeList

    def dualTypeSuperEffective(self,type1,type2):
        #Everything type1/type2 is weak against, gets hit with super effective attacks
        types = pokemonTypeWeakness.TypeWeakness()
        typeList = []
        t1 = getattr(types, type1.lower())
        t2 = getattr(types, type2.lower())
        for i in self.typesList:
            if t1(i)*t2(i)> 1 and i not in typeList:
                typeList.append(i)
            for j in self.typesList:
                dualType = i+"/"+j
                if((t1(j)*t2(j) > 1 or t1(i)*t2(i)>1) and dualType not in typeList and i != j):
                    typeList.append(dualType)
        return typeList

    def monoTypeStrengths(self,type1,damage):
        #Everything type1 is not strong against, deals neutral damage or less
        types = pokemonTypeWeakness.TypeWeakness()
        typeList = []
        for i in self.typesList:
            t1 = getattr(types, i.lower())
            if t1(type1) <= damage and i not in typeList:
                typeList.append(i)
            for j in self.typesList:
                t2 = getattr(types, j.lower())
                dualType = i+"/"+j
                if(t1(type1)*t2(type1) <= damage and dualType not in typeList and i != j):
                    typeList.append(dualType)
        return typeList

    def teraTypeStrengths(self,type1):
        #Everything teraType strong against, deals super effective damage
        types = pokemonTypeWeakness.TypeWeakness()
        typeList = []
        #Need to work on for loop. Get all values of the tera type > 1 on all types plus dual types.
        for i in self.typesList:
            #check how does type1 peform against all mono types
            t1 = getattr(types, i.lower())
            if t1(i) > 1 and i not in typeList:
                typeList.append(i)
            #check how does type1 perform against all dual types
            for j in self.typesList:
                t2 = getattr(types, j.lower())
                dualType = i+"/"+j
                if(t1(type1)*t2(type1) > 1 and dualType not in typeList and i != j):
                    typeList.append(dualType)
        return typeList

    def dualTypeStrengths(self,type1,type2,damage1=0.5,damage2=0.5):
        #Everything type1/type2 is not strong against, deals neutral damage or less
        types = pokemonTypeWeakness.TypeWeakness()
        typeList = []
        for i in self.typesList:
            t1 = getattr(types, i.lower())
            if t1(type1) <= damage1 and t1(type2) <= damage2 and i not in typeList:
                typeList.append(i)
            if t1(type2) <= damage1 and t1(type1) <= damage2 and i not in typeList:
                typeList.append(i)
            for j in self.typesList:
                t2 = getattr(types, j.lower())
                dualType = i+"/"+j
                if(t1(type1)*t2(type1)<=damage1 and t1(type2)*t2(type2)<=damage2 and dualType not in typeList and i!=j):
                    typeList.append(dualType)
                elif(t1(type2)*t2(type2)<=damage1 and t1(type1)*t2(type1)<=damage2 and dualType not in typeList and i!=j):
                    typeList.append(dualType)
        #for i in typeList:
        #    print(i)
        return typeList
    

    def dualTypeCounter(self,type1,type2,damage1,damage2):
        #Want to have super effetive moves (2,4 times damage) 
        #Want to avoid taking super effective moves (2,4 times damage)
        if type2 != "":
            counterDefense = self.dualTypeStrengths(type1,type2,damage1,damage2)
            counterOffense = self.dualTypeSuperEffective(type1,type2)
        else:
            counterDefense = self.monoTypeStrengths(type1,damage1)
            counterOffense = self.monoTypeSuperEffective(type1)
        combo = []
        for i in counterOffense:
            if i in counterDefense and i not in combo:
                combo.append(i)
        return combo

    def avoidTeraType(self,combo,teraType,damage):
        #Get a list of all damage the teraType deals against other types
        #To avoid tera type we need to get a list of all combinations that the type isn't effective against
        #Then compare the combo list of all types resistant to the base type to the avoid tera type
        teraBlast = self.monoTypeStrengths(teraType,damage[0])
        teraStrength = self.teraTypeStrengths(teraType)
        avoidTeraBlast = []
        for i in combo:
            for j in teraBlast:
                if i in j and i not in avoidTeraBlast:
                    avoidTeraBlast.append(i)
        for i in avoidTeraBlast:
            for j in teraStrength:
                if i == j:
                    avoidTeraBlast.remove(j)
        return avoidTeraBlast

    def teraTypeCounter(self,pokemon,teraType,damage):
        #type1/type2 is the types to defend against
        #teraType is the type we want to be most effective against
        type1 = pokemon[2]
        type2 = pokemon[3]
        damage1 = damage[0]
        damage2 = damage[1]
        #if there isn't a second type, check what the mono typing is not strong against
        if type2 == "":
            counterDefense = self.monoTypeStrengths(type1,damage1)
        #Otherwise check what both typings are not strong against
        else:
            counterDefense = self.dualTypeStrengths(type1,type2,damage1,damage2)
        #Next we want to get a list of pokemon typings that will be super effective against the tera type
        counterOffense = self.monoTypeSuperEffective(teraType)
        #Now combine the two for most defensive+super effective against tera pokemon type
        combo = []
        for i in counterOffense:
            if i in counterDefense and i not in combo:
                combo.append(i)
        return combo

def main():
    dualType = DualType()
    while True:
        type1 = input("Enter the first type or q to quit: ").strip().lower().capitalize()
        if(type1 == "Q"): 
            break
        type2 = input("Enter second type or q to quit: ").strip().lower().capitalize()
        if(type2 == "Q"):
            break
        teraType = input("Tera type for pokemon: ").strip().lower().capitalize()
        if(teraType == "Q"):
            break
        print("Chose an option for number of pokemon types to list for defensive purposes.")
        print(" 1: Neutral/Neutral: ")
        print(" 2: Neutral/Resistant: ")
        print(" 3: Neutral/Very Resistant: ")
        print(" 4: Neutral/No Damage: ")
        print(" 5: Resistant/Resistant: ")
        print(" 6: Resistant/Very Resistant: ")
        print(" 7: Resistant/No Damage: ")
        print(" 8: Very Resistant/Very Resistant: ")
        print(" 9: Very Resistant/No Damage: ")
        print("10: No damage ")
        try:
            defensiveness = int(input())
        except:
            defensiveness = 1
        if(defensiveness == "Q"):
            break
        damage1 = 1
        damage2 = 1
        if (defensiveness == 2):
            damage2 = 0.5
        elif (defensiveness == 3):
            damage2 = 0.25
        elif (defensiveness == 4):
            damage2 = 0
        elif (defensiveness == 5):
            damage1 = 0.5
            damage2 = 0.5
        elif (defensiveness == 6):
            damage1 = 0.5
            damage2 = 0.25
        elif (defensiveness == 7):
            damage1 = 0.5
            damage2 = 0
        elif (defensiveness == 8):
            damage1 = 0.25
            damage2 = 0.25
        elif (defensiveness == 9):
            damage1 = 0.25
            damage2 = 0
        elif (defensiveness == 10):
            damage1 = 0
            damage2 = 0
        if teraType != "":
            selection = dualType.teraTypeCounter(["","",type1,type2],teraType,[damage1,damage2],True)
            for i in selection:
                print(i)
        else:
            selection = dualType.dualTypeCounter(type1,type2,damage1,damage2)
            for i in selection:
                print(i)

#if __name__=="__main__":
#    main()
    #dualTypes = DualType()
    #dualTypes.dualTypeWeakness("Dark","Ice")
