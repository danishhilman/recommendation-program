from data import pokedex

#prints all pokemon mapped to their respective type and stats
def display_pokemon_list(pokemon_list=pokedex):

    for i in pokemon_list:
        print("{pokemon}\n Type: {type}\n Stats: {stats}\n".format(pokemon=i, type=pokemon_list[i]["Type"], stats=pokemon_list[i]["Stats"]))

#if a pokemon name starts with the specified letter/word; returns a dictionary with the pokemon mapped to their respective type and stats
def pokemon_by_starting_letter(letter, pokemon_list=pokedex):

    sorted_pokemon = {}
    for i in sorted(pokemon_list):
        if i.startswith(str(letter).title()):
            sorted_pokemon[i] = {"Type":pokemon_list[i]["Type"], "Stats":pokemon_list[i]["Stats"]}
    return sorted_pokemon

#returns a dictionary of all the pokemon which has the specified type OR returns a list of all pokemon with only the specified type
def pokemon_with_type(*type, only_type=False, pokemon_list=pokedex):

    sorted_pokemon = {}
    type = list(type)
    for i in pokemon_list:
        #adds all pokemon with only the specified type
        if only_type == True:
            if all(x in pokemon_list[i]["Type"] for x in type) and len(pokemon_list[i]["Type"]) == 1:
                sorted_pokemon[i] = {"Type":pokemon_list[i]["Type"], "Stats":pokemon_list[i]["Stats"]}

        #adds all pokemon with the specified type combinations
        elif len(type) == 2:
            if all(x in pokemon_list[i]["Type"] for x in type) and len(pokemon_list[i]["Type"]) == 2:
                sorted_pokemon[i] = {"Type":pokemon_list[i]["Type"], "Stats":pokemon_list[i]["Stats"]}

        #adds all pokemon with the specified type regardless of other type
        elif all(x in pokemon_list[i]["Type"] for x in type):
            sorted_pokemon[i] = {"Type":pokemon_list[i]["Type"], "Stats":pokemon_list[i]["Stats"]}
    return sorted_pokemon

#returns a dictionary of all the pokemon with a specified stats category with a maximum value, minimum value or specific value
def pokemon_with_stats(stat_type, val, min=False, max=False, pokemon_list=pokedex):
    
    sorted_pokemon = {}
    for i in pokemon_list:
        if min == True:
            if pokemon_list[i]["Stats"][stat_type] >= val:
                sorted_pokemon[i] = {"Type":pokemon_list[i]["Type"], "Stats":pokemon_list[i]["Stats"]}
        elif max == True: 
            if pokemon_list[i]["Stats"][stat_type] <= val:
                sorted_pokemon[i] = {"Type":pokemon_list[i]["Type"], "Stats":pokemon_list[i]["Stats"]}
        else:
            if pokemon_list[i]["Stats"][stat_type] == val:
                sorted_pokemon[i] = {"Type":pokemon_list[i]["Type"], "Stats":pokemon_list[i]["Stats"]}

    sorted_pokemon = dict(sorted(sorted_pokemon.items(), key=lambda item: item[1]["Stats"][stat_type]))
    return sorted_pokemon

    
# pokemon_by_starting_letter("Partner")
# pokemon_with_type("WATER", "ICE")
# pokemon_with_stats("Speed", 100, max=True)
# display_pokemon_list(pokemon_list=pokemon_with_type("WATER", pokemon_list=pokemon_with_stats("Total", 600, max=True)))
# display_pokemon_list(pokemon_list=pokemon_with_type("WATER", pokemon_list=pokemon_by_starting_letter("A")))
display_pokemon_list(pokemon_list=pokemon_with_type("GHOST", pokemon_list=pokemon_with_stats("Total", 600)))
