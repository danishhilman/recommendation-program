import csv

pokedex = []
with open("pokedex.csv", newline="") as pokedex_csv:
  pokedex_reader = csv.DictReader(pokedex_csv, delimiter=",")
  for row in pokedex_reader:
    pokedex.append(row)

def get_all_pokemon_name():
        pokemon_name = []
        index = 0
        for i in pokedex:
            
            if i["ï»¿#"] == "":
                pass
            
            elif i["ï»¿#"].startswith("Mega"):
                pokemon_name.append(pokedex[index + 1]["Name"])

            else:
                pokemon_name.append(i["Name"])
            index += 1
        return pokemon_name

def get_all_pokemon_name_and_type():
        all_pokemon_names_and_type = {x: None for x in get_all_pokemon_name()}
        index = 0
        for i in all_pokemon_names_and_type:
            all_pokemon_names_and_type[i] = [pokedex[index]["Type"]]
            if pokedex[index+1]["ï»¿#"] == "":
                if pokedex[index+1]["Type"] != "":
                    all_pokemon_names_and_type[i].append(pokedex[index + 1]["Type"])
                    index += 1
                else:
                    index += 1
            index += 1
        return all_pokemon_names_and_type
            

