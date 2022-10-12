from data import get_all_pokemon_name, get_all_pokemon_name_and_type, get_all_pokemon_name_and_stats, get_all_pokemon_name_type_stats, pokedex

# print(get_all_pokemon_name())
# print(get_all_pokemon_name_and_type())

def pokemon_by_starting_letter(letter):

    for i in sorted(get_all_pokemon_name_and_type()):
        if i.startswith(str(letter).title()):
            print(i, get_all_pokemon_name_and_type()[i])

# pokemon_by_starting_letter("Ag")
# print(get_all_pokemon_name_and_stats())
# print(get_all_pokemon_name_type_stats())