# Pokemon
A repository for developing out features I would like to make easier for when I play pokemon

1.Currently features:
  - Mono typing weakness class
  - Dual typing weakness class
    - functions: dualTypeStrengths
      - calculates what typeStrengths are effective against the pokemon of choice
        - for instance: If pokemon typing is Dark/Fire, lists all types that are defensive against Dark/Fire
    - functions: monoTypeStrengths
      - calculates similar to dualTypeStrengths except is for just one type.
    - functions: dualTypeSuperEffective
      - calculates all types that deal 2x or more damage to a dual typing opponent pokemon
    - functions: monoTypeSuperEffective
      - calculates all types that deal 2x or more damage to a single typing opponent pokemon
    - functions: teraTypeCounter
      - calculates which pokemon are most defensive against a pokemon mono/dual typing and are most effective against that pokemons tera typing

- [] Need to implement avoiding tera blast
- [] Need to implement csv reader for listing pokemon effective against typing + tera
- [] Need to implement listing all options for all defensives against typing
     1. Neutral/Neutral
     2. Neutral/Resistant
     3. Neutral/Very Resistant
     4. Neutral/No Damage
     5. Resistant/Resistant
     5. Resistant/Very Resistant
     6. Resistant/No Damage
     7. Very Resistant/Very Resistant
     8. Very Resistant/No Damage
     9. No Damage/No Damage
     
- [] Need to implement typing in tera raid pokemon and generating list of pokemon
- [] Need to create function to determine which offensive stat is best against tera raid pokemon
