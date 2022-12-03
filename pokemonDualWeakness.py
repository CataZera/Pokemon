#!/usr/bin/env python3
###Class is for a list of defined dual type weaknesses against singular types and other dual types

import sys
import pokemonTypeWeakness
import pdb
class DualType(object):

    typesList = ["Normal","Fire","Water","Electric","Grass","Ice",
                 "Fighting","Poison","Ground","Flying","Psychic","Bug",
                 "Rock","Ghost","Dragon","Dark","Steel","Fairy"]

    debug = True

    def dualTypeWeakness(self,type1,type2):
        #Everything this type is weak against
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
        #if(self.debug):
        #    print(len(typeList), " deal super effective damage to " + type1)
        #    for i in typeList:
        #        print(i)
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
        #if(self.debug):
        #    print(len(typeList), " deal super effective damage to " + type1 + "/" + type2)
        #    for i in typeList:
        #        print(i)
        return typeList

    def monoTypeStrengths(self,type1,damage1=0.5,damage2=0.5):
        #Everything type1 is not strong against, deals neutral damage or less
        types = pokemonTypeWeakness.TypeWeakness()
        typeList = []
        for i in self.typesList:
            t1 = getattr(types, i.lower())
            if t1(type1) <= damage1 and i not in typeList:
                typeList.append(i)
            for j in self.typesList:
                t2 = getattr(types, j.lower())
                dualType = i+"/"+j
                if(t1(type1)*t2(type1) <= damage1 and dualType not in typeList and i != j):
                    typeList.append(dualType)
        
        #if(self.debug):
        #    print(len(typeList), " are resistant to " + type1)
        #    for i in typeList:
        #        print(i)
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
                if(t1(type1)*t2(type1) <= damage1 and t1(type2)*t2(type2) <=damage2 and dualType not in typeList and i != j):
                    typeList.append(dualType)
        #if(self.debug):
        #    print(len(typeList), " are resistant to " + type1 + "/" + type2)
        #    for i in typeList:
        #        print(i)
        return typeList
    

    def dualTypeCounter(self,type1,type2,damage1,damage2):
        #Want to have super effetive moves (2,4 times damage) 
        #Want to avoid taking super effective moves (2,4 times damage)
        #EX: If enemy pokemon is Dark/Steel type then want to choose:
        #Fighting, Fire, or Ground Pokemon moves or typing to be super effective or have tera typing of this.
        #Want to avoid on the other hand:
        #Dozens of type combinations that I won't list because there are too many
        #Ideally create a list of pokemon that take neutral damage or less and deal super effective damage.
        counterDefense = self.dualTypeStrengths(type1,type2,damage1,damage2)
        counterOffense = self.dualTypeSuperEffective(type1,type2)
        combo = []
        for i in counterOffense:
            if i in counterDefense and i not in combo:
                combo.append(i)
        #if (self.debug):
        #    print()
        #    print(len(combo), "types that are super effective and resistant against " + type1+"/"+type2)
        #    for i in combo:
        #        print(i)
        return combo

    def avoidTeraBlast(self,type1,type2,teratype,damage1,damage2):
        pass

    def teraTypeCounter(self,pokemon,teraType,damage,avoidTeraType=False):
        #type1/type2 is the types to defend against
        #teraType is the type we want to be most effective against
        #combine this that means we want the best defense against type1/type2, yet be strongest against teraType
        type1 = pokemon[2]
        type2 = pokemon[3]
        damage1 = damage[0]
        damage2 = damage[1]
        if type2 == "":
            counterDefense = self.monoTypeStrengths(type1,damage1,damage2)
        else:
            counterDefense = self.dualTypeStrengths(type1,type2,damage1,damage2)
        counterOffense = self.monoTypeSuperEffective(teraType)
        combo = []
        for i in counterOffense:
            if i in counterDefense and i not in combo:
                combo.append(i)
        #Add check case for when avoidTeraBlast is true
        #remove the pokemon from the combo list that are weak to the tera typing
        #Return the new result of the pokemon list
        if avoidTeraType:
            index = 0
            teraBlast = self.dualTypeWeakness(teraType,"")
            avoidTeraBlast = []
            for i in range(len(teraBlast)-1):
                if type(teraBlast[i]) !=  str and teraBlast[i] > 1:
                    avoidTeraBlast.append(teraBlast[i-1])
            tmp = []
            for i in avoidTeraBlast:
                for j in combo:
                    if i in j:
                        tmp.append(j)

            for i in tmp:
                if i in combo:
                    combo.remove(i)
        if(self.debug):
            print()
            if (type2 == ""):
                print(len(combo), "types that are super effective against tera " + teraType+ " and resistant to base type " + type1)
                for i in combo:
                    print(i)
            else:
                print(len(combo), "types that are super effective against tera " + teraType+ " and resistant to base type " + type1+"/"+type2)
                for i in combo:
                    print(i)
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
            dualType.teraTypeCounter(["","",type1,type2],teraType,[damage1,damage2])
        else:
            if(type1 == ""):
                type1 = type2
                type2 = ""
            dualType.dualTypeCounter(type1,type2,damage1,damage2)

if __name__=="__main__":
    main()
    #dualTypes = DualType()
    #dualTypes.dualTypeWeakness("Dark","Ice")
