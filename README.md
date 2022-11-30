# Pokemon
A repository for developing out features I would like to make easier for when I play pokemon

Currently features:
  Mono typing weakness class
  Dual typing weakness class
    functions: dualTypeStrengths
       calculates what typeStrengths are effective against the pokemon of choice
       for instance: If pokemon typing is Dark/Fire, lists all types that are defensive against Dark/Fire
    functions: monoTypeStrengths
        calculates similar to dualTypeStrengths except is for just one type.
    functions: dualTypeSuperEffective
        calculates all types that deal 2x or more damage to a dual typing opponent pokemon
    functions: monoTypeSuperEffective
        calculates all types that deal 2x or more damage to a single typing opponent pokemon
    functions: teraTypeCounter
        calculates which pokemon are ideal against a pokemon mono/dual typing and are most effective against that pokemons tera typing
