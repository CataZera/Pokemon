#include <iostream>
#include <string>
#include <iomanip>

class TypeWeakness{
    
    public:
        double bug(std::string type){
            double damage = 1.0;
            if (type == "Fire" || type == "Flying" || type == "Rock"){
                damage = 2.0;
            } else if (type == "Fighting" || type == "Grass" || type == "Ground"){
                damage = 0.5;    
            }
            return damage;
        }
        
        double dark(std::string type){
            double damage = 1.0;
            if (type == "Bug" || type == "Fairy" || type == "Fighting"){
                damage = 2.0;
            } else if (type == "Dark" || type == "Ghost"){
                damage = 0.5;
            } else if (type == "Psychic") {
                damage = 0;
            }
            return damage;
        }
        
        double dragon(std::string type){
            double damage = 1.0;
            if (type == "Dragon" || type == "Fairy" || type == "Ice"){
                damage = 2.0;
            } else if (type == "Electric" || type == "Fire" || 
                       type == "Grass" || type == "Water"){
                damage = 0.5;
            }
            return damage;
        }

        double electric(std::string type){
            double damage = 1.0;
            if (type == "Ground") {
                damage = 2.0;
            } else if (type == "Electric" || type == "Flying" || type == "Steel"){
                damage = 0.5;
            }
            return damage;
        }

        double fairy(std::string type){
            double damage = 1;
            if (type == "Poison" || type == "Steel"){
                damage = 2;
            } else if (type == "Bug" || type == "Dark" || type == "Fighting"){
                damage = 0.5;
            } else if (type == "Dragon"){
                damage = 0;
            }
            return damage;
        }
        
        double fighting(std::string type){
            double damage = 1;
            if (type == "Fairy" || type == "Flying" || type == "Psychic"){
                damage = 2;
            } else if (type == "Bug" || type == "Dark" || type == "Rock"){
                damage = 0.5;
            }
            return damage;
        }

        double fire(std::string type){
            double damage = 1;
            if (type == "Ground" || type == "Rock" || type == "Water"){
                damage = 2;
            } else if (type == "Bug" || type == "Fairy" || type == "Fire" || 
                       type == "Grass" || type == "Ice" || type == "Steel"){
                damage = 0.5;
            }
            return damage;
        }

        double flying(std::string type){
            double damage = 1;
            if (type == "Electric" || type == "Ice" || type == "Rock"){
                damage = 2;
            } else if (type == "Bug" || type == "Fighting" || type == "Grass"){
                damage = 0.5;
            } else if (type == "Ground"){
                damage = 0;
            }
            return damage;
        }

        double ghost(std::string type){
            double damage = 1;
            if (type == "Dark" || type == "Ghost"){
                damage = 2;
            } else if (type == "Bug" || type == "Poison"){
                damage = 0.5;
            } else if (type == "Fighting" || type == "Normal"){
                damage = 0;
            }
            return damage;
        }

        double grass(std::string type){
            double damage = 1;
            if (type == "Bug" || type == "Fire" || type == "Flying" ||
                type == "Ice" || type == "Poison"){
                damage = 2;
            } else if (type == "Electricity" || type == "Grass" || 
                       type == "Ground" || type == "Water"){
                damage = 0.5;
            }
            return damage;
        }

        double ground(std::string type){
            double damage = 1;
            if (type == "Grass" || type == "Ice" || type == "Water"){
                damage = 2;
            } else if (type == "Poison" || type == "Rock"){
                damage = 0.5;
            } else if (type == "Electricity"){
                damage = 0;
            }
            return damage;
        }
        
        double ice(std::string type){
            double damage = 1;
            if (type == "Fighting" || type == "Fire" || type == "Rock" || type == "Steel"){
                damage = 2;
            } else if (type == "Ice"){
                damage = 0.5;
            }
            return damage;
        }

        double normal(std::string type){
            double damage = 1;
            if (type == "Fighting"){
                damage = 2;
            } else if (type == "Ghost"){
                damage = 0;
            }
            return damage;
        }

        double poison(std::string type){
            double damage = 1;
            if (type == "Ground" || type == "Psychic"){
                damage = 2;
            } else if (type == "Bug" || type == "Fairy" || type == "Fighting" ||
                       type == "Grass" || type == "Poison"){
                damage = 0.5;
            }
            return damage;
        }

        double psychic(std::string type){
            double damage = 1;
            if (type == "Bug" || type == "Dark" || type == "Ghost"){
                damage = 2;
            } else if (type == "Fighting" || type == "Psychic"){
                damage = 0.5;
            }
            return damage;
        }

        double rock(std::string type){
            double damage = 1;
            if (type == "Fighting" || type == "Grass" || type == "Ground" ||
                type == "Steel" || type == "Water"){
                damage = 2;
            } else if (type == "Fire" || type == "Flying" || type == "Normal" || type == "Poison"){
                damage = 0.5;
            }
            return damage;
        }

        double steel(std::string type){
            double damage = 0.5;
            if (type == "Fighting" || type == "Fire" || type == "Ground"){
                damage = 2;
            } else if (type == "Dark" || type == "Electric" || type == "Ghost" || type == "Water"){
                damage = 1;
            } else if (type == "Poison"){
                damage = 0;
            }
            return damage;
        }

        double water(std::string type){
            double damage = 1;
            if (type == "Electric" || type == "Grass"){
                damage = 2;
            } else if (type == "Fire" || type == "Ice" || type == "Steel" || type == "Water"){
                damage = 0.5;
            }
            return damage;
        }

        bool verifyAttackType(std::string type){
            std::string arr[18] = {"Bug","Dark","Dragon","Electric","Fairy","Fighting",
                                   "Fire","Flying","Ghost","Grass","Ground","Ice",
                                   "Normal","Poison","Psychic","Rock","Steel","Water"
                                  };
            for (int i = 0; i < 18; i++){
                if (arr[i] == type){
                    return true;
                }
            }
            return false;   
        }
};


int main(){
    TypeWeakness tw;
    double value = tw.bug("Fire");
    double value2 = tw.dragon("Water");
    std::string type = "normal";
    if (!tw.verifyAttackType(type)){
        std::cout << "Attack does not match any of the typings." << std::endl;
        std::cout << "Make sure the spelling is correct and the first letter is capitalized." << 
        std::endl;
        std::cout << "Value given: " + type << std::endl;
    }
    std::cout << value * value2 << std::endl;
    return 0;
}
