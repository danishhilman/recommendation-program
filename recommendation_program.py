from data import get_all_pokemon_name, get_all_pokemon_name_and_type, get_all_pokemon_name_and_stats, get_all_pokemon_name_type_stats, pokedex

# print(get_all_pokemon_name())
# print(get_all_pokemon_name_and_type())
# print(get_all_pokemon_name_and_stats())
# print(get_all_pokemon_name_type_stats())

#prints all pokemon mapped to their respective type and stats
def display_all_pokemon():

    all_pokemon = get_all_pokemon_name_type_stats()
    for i in all_pokemon:
        print("{pokemon}\n Type: {type}\n Stats: {stats}\n".format(pokemon=i, type=all_pokemon[i]["Type"], stats=all_pokemon[i]["Stats"]))

#if a pokemon name starts with the specified letter/word; prints the pokemon mapped to their respective type and stats
def pokemon_by_starting_letter(letter):

    all_pokemon = get_all_pokemon_name_type_stats()
    for i in sorted(all_pokemon):
        if i.startswith(str(letter).title()):
            print("{pokemon}\n Type: {type}\n Stats: {stats}\n".format(pokemon=i, type=all_pokemon[i]["Type"], stats=all_pokemon[i]["Stats"]))

#prints all pokemon which has the specified type OR prints all pokemon with only the specified type
def pokemon_with_type(type, only_type=False):

    all_pokemon = get_all_pokemon_name_type_stats()
    for i in all_pokemon:
        #prints all pokemon with only the specified
        if only_type == True:
            if type in all_pokemon[i]["Type"] and len(all_pokemon[i]["Type"]) == 1:
                print("{pokemon}\n Type: {type}\n Stats: {stats}\n".format(pokemon=i, type=all_pokemon[i]["Type"], stats=all_pokemon[i]["Stats"]))

        #prints all pokemon with the specified type regardless of other type
        elif type in all_pokemon[i]["Type"]:
                print("{pokemon}\n Type: {type}\n Stats: {stats}\n".format(pokemon=i, type=all_pokemon[i]["Type"], stats=all_pokemon[i]["Stats"]))

#prints all pokemon with a specified stats category with a maximum value, minimum value or specific value
def pokemon_with_stats(stat_type, val, min=False, max=False):
    all_pokemon = get_all_pokemon_name_type_stats()
    pokemon_stats_dict = {}
    for i in all_pokemon:
        if min == True:
            if all_pokemon[i]["Stats"][stat_type] >= val:
                pokemon_stats_dict[i] = all_pokemon[i]["Stats"][stat_type]
        elif max == True: 
            if all_pokemon[i]["Stats"][stat_type] <= val:
                pokemon_stats_dict[i] = all_pokemon[i]["Stats"][stat_type]
        else:
            if all_pokemon[i]["Stats"][stat_type] == val:
                pokemon_stats_dict[i] = all_pokemon[i]["Stats"][stat_type]

    pokemon_stats_dict = dict(sorted(pokemon_stats_dict.items(), key=lambda item: item[1]))
    
    for i in pokemon_stats_dict:
        print("{pokemon}\n Type: {type}\n Stats: {stats}\n".format(pokemon=i, type=all_pokemon[i]["Type"], stats=all_pokemon[i]["Stats"]))
    

# pokemon_by_starting_letter("D")
# pokemon_with_type("FIRE")
pokemon_with_stats("Speed", 100, max=True)
# display_all_pokemon()
# print(get_all_pokemon_name_type_stats())
