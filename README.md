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
2. Created pokedex class:
   - Features retrieving pokemon from csv file.
   - Finding the best pokemon against the tera raid pokemon
   - Can find the best pokemon avoiding the typind of the pokemon in addition to the tera typing:
     - Avoiding tera type is beneficial to avoid tera blast and stab resultant of that
   - Can specify through combined base stats at what amount to list as most effective 


- [x] Need to implement avoiding tera blast
- [x] Need to implement csv reader for listing pokemon effective against typing + tera
- [x] Need to implement listing all options for all defensives against typing
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
     
- [x] Need to implement typing in tera raid pokemon and generating list of pokemon
- [] Need to create function to determine which offensive stat is best against tera raid pokemon
- [x] Need to create function to iterate through all defensive levels and return list of pokemon that are most resistant
- [] Need to create a GUI for easier interaction.
     - [] Create a list of tera raid pokemon
     - [] Incorporate images for ease of identifying pokemon
     - [] Selection for tera type
     - [] Defensive level option or display highest resistant pokemon
