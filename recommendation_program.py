from data import get_all_pokemon_name, get_all_pokemon_name_and_type, get_all_pokemon_name_and_stats, get_all_pokemon_name_type_stats, pokedex

# print(get_all_pokemon_name())
# print(get_all_pokemon_name_and_type())
# print(get_all_pokemon_name_and_stats())
# print(get_all_pokemon_name_type_stats())

def pokemon_by_starting_letter(letter):

    for i in sorted(get_all_pokemon_name_and_type()):
        if i.startswith(str(letter).title()):
            print(i, get_all_pokemon_name_and_type()[i])

def pokemon_with_type(type, only_type=False):
    
    for i in get_all_pokemon_name_and_type():
        if only_type == True:
            if type in get_all_pokemon_name_and_type()[i] and len(get_all_pokemon_name_and_type()[i]) == 1:
                print(i, get_all_pokemon_name_and_type()[i])

        elif type in get_all_pokemon_name_and_type()[i]:
            print(i, get_all_pokemon_name_and_type()[i])

def pokemon_with_stats(stat_type, val, min=False, max=False):
    pokemon_stats_dict = {}
    for i in get_all_pokemon_name_and_stats():
        if get_all_pokemon_name_and_stats()[i][stat_type] >= val:
            pokemon_stats_dict[i] = get_all_pokemon_name_and_stats()[i][stat_type]
    sorted_pokemon_stats_dict = dict(sorted(pokemon_stats_dict.items(), key=lambda item: item[1]))
    print(sorted_pokemon_stats_dict)

# pokemon_by_starting_letter("D")
# pokemon_with_type("FIRE", True)
# pokemon_with_stats("Speed", 100)