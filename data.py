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
            
            elif i["ï»¿#"].startswith("Mega "):
                pokemon_name.append(pokedex[index + 1]["Name"])

            elif i["ï»¿#"].startswith("Alolan"):
                pokemon_name.append(pokedex[index + 1]["Name"])
            
            elif i["ï»¿#"].startswith("Galarian"):
                pokemon_name.append(pokedex[index + 1]["Name"])
            
            elif i["ï»¿#"].startswith("Primal "):
                pokemon_name.append(pokedex[index + 1]["Name"])
            
            elif ("(Female)") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index]["Name"] + " " + pokedex[index + 1]["Name"])

            elif ("(Male)") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index]["Name"] + " " + pokedex[index + 1]["Name"])

            elif ("Hisuian") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])

            elif ("Partner") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])

            elif ("Heat Rotom") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])
            
            elif ("Wash Rotom") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])

            elif ("Frost Rotom") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])

            elif ("Fan Rotom") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])
            
            elif ("Mow Rotom") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])
            
            elif ("Kyurem (White Kyurem)") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])

            elif ("Kyurem (Black Kyurem)") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])

            elif ("Greninja (Ash-Greninja)") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])
            
            elif ("Hoopa (Hoopa Confined)") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])

            elif ("Hoopa (Hoopa Unbound)") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])
            
            elif ("(Own Tempo Rockruff)") in i["ï»¿#"]:
                pokemon_name.append(pokedex[index + 1]["Name"])

            elif ("Sunny ") in i["ï»¿#"]:
                pokemon_name.append("Castform " + pokedex[index + 1]["Name"])
            
            elif ("Rainy ") in i["ï»¿#"]:
                pokemon_name.append("Castform " + pokedex[index + 1]["Name"])
            
            elif ("Snowy ") in i["ï»¿#"]:
                pokemon_name.append("Castform " + pokedex[index + 1]["Name"])

            elif ("Normal Forme") in i["ï»¿#"]:
                pokemon_name.append("Deoxys " + pokedex[index + 1]["Name"])
            
            elif ("Attack Forme") in i["ï»¿#"]:
                pokemon_name.append("Deoxys " + pokedex[index + 1]["Name"])

            elif ("Defense Forme") in i["ï»¿#"]:
                pokemon_name.append("Deoxys " + pokedex[index + 1]["Name"])

            elif ("Speed Forme") in i["ï»¿#"]:
                pokemon_name.append("Deoxys " + pokedex[index + 1]["Name"])

            elif ("Burmy (Plant Cloak)") in i["ï»¿#"]:
                pokemon_name.append("Burmy " + pokedex[index + 1]["Name"])

            elif ("Burmy (Sandy Cloak)") in i["ï»¿#"]:
                pokemon_name.append("Burmy " + pokedex[index + 1]["Name"])

            elif ("Burmy (Trash Cloak)") in i["ï»¿#"]:
                pokemon_name.append("Burmy " + pokedex[index + 1]["Name"])

            elif ("Wormadam (Plant Cloak)") in i["ï»¿#"]:
                pokemon_name.append("Wormadam " + pokedex[index + 1]["Name"])
            
            elif ("Wormadam (Sandy Cloak)") in i["ï»¿#"]:
                pokemon_name.append("Wormadam " + pokedex[index + 1]["Name"])
            
            elif ("Wormadam (Trash Cloak)") in i["ï»¿#"]:
                pokemon_name.append("Wormadam " + pokedex[index + 1]["Name"])

            elif ("Dialga (Origin Forme)") in i["ï»¿#"]:
                pokemon_name.append("Dialga " + pokedex[index + 1]["Name"])

            elif ("Palkia (Origin Forme)") in i["ï»¿#"]:
                pokemon_name.append("Palkia " + pokedex[index + 1]["Name"])
            
            elif ("Giratina (Altered Forme)") in i["ï»¿#"]:
                pokemon_name.append("Giratina " + pokedex[index + 1]["Name"])
            
            elif ("Giratina (Origin Forme)") in i["ï»¿#"]:
                pokemon_name.append("Giratina " + pokedex[index + 1]["Name"])
            
            elif ("Shaymin (Land Forme)") in i["ï»¿#"]:
                pokemon_name.append("Shaymin " + pokedex[index + 1]["Name"])

            elif ("Shaymin (Sky Forme)") in i["ï»¿#"]:
                pokemon_name.append("Shaymin " + pokedex[index + 1]["Name"])
            
            elif ("Basculin (Red-Striped Form)") in i["ï»¿#"]:
                pokemon_name.append("Basculin " + pokedex[index + 1]["Name"])

            elif ("Basculin (Blue-Striped Form)") in i["ï»¿#"]:
                pokemon_name.append("Basculin " + pokedex[index + 1]["Name"])

            elif ("Basculin (White-Striped Form)") in i["ï»¿#"]:
                pokemon_name.append("Basculin " + pokedex[index + 1]["Name"])
            
            elif ("Darmanitan (Standard Mode)") in i["ï»¿#"]:
                pokemon_name.append("Darmanitan " + pokedex[index + 1]["Name"])

            elif ("Darmanitan (Zen Mode)") in i["ï»¿#"]:
                pokemon_name.append("Darmanitan " + pokedex[index + 1]["Name"])

            elif ("Darmanitan (Galarian Standard Mode)") in i["ï»¿#"]:
                pokemon_name.append("Darmanitan " + pokedex[index + 1]["Name"])

            elif ("Darmanitan (Galarian Zen Mode)") in i["ï»¿#"]:
                pokemon_name.append("Darmanitan " + pokedex[index + 1]["Name"])
            
            elif ("Tornadus (Incarnate Forme)") in i["ï»¿#"]:
                pokemon_name.append("Tornadus " + pokedex[index + 1]["Name"])

            elif ("Tornadus (Therian Forme)") in i["ï»¿#"]:
                pokemon_name.append("Tornadus " + pokedex[index + 1]["Name"])

            elif ("Thundurus (Incarnate Forme)") in i["ï»¿#"]:
                pokemon_name.append("Thundurus " + pokedex[index + 1]["Name"])

            elif ("Thundurus (Therian Forme)") in i["ï»¿#"]:
                pokemon_name.append("Thundurus " + pokedex[index + 1]["Name"])

            elif ("Landorus (Incarnate Forme)") in i["ï»¿#"]:
                pokemon_name.append("Landorus " + pokedex[index + 1]["Name"])

            elif ("Landorus (Therian Forme)") in i["ï»¿#"]:
                pokemon_name.append("Landorus " + pokedex[index + 1]["Name"])
            
            elif ("Keldeo (Ordinary Form)") in i["ï»¿#"]:
                pokemon_name.append("Keldeo " + pokedex[index + 1]["Name"])

            elif ("Keldeo (Resolute Form)") in i["ï»¿#"]:
                pokemon_name.append("Keldeo " + pokedex[index + 1]["Name"])

            elif ("Meloetta (Aria Forme)") in i["ï»¿#"]:
                pokemon_name.append("Meloetta " + pokedex[index + 1]["Name"])
            
            elif ("Meloetta (Pirouette Forme)") in i["ï»¿#"]:
                pokemon_name.append("Meloetta " + pokedex[index + 1]["Name"])

            elif ("Aegislash (Shield Forme)") in i["ï»¿#"]:
                pokemon_name.append("Aegislash " + pokedex[index + 1]["Name"])

            elif ("Aegislash (Blade Forme)") in i["ï»¿#"]:
                pokemon_name.append("Aegislash " + pokedex[index + 1]["Name"])

            elif ("Pumpkaboo (Average Size)") in i["ï»¿#"]:
                pokemon_name.append("Pumpkaboo " + pokedex[index + 1]["Name"])

            elif ("Pumpkaboo (Small Size)") in i["ï»¿#"]:
                pokemon_name.append("Pumpkaboo " + pokedex[index + 1]["Name"])
            
            elif ("Pumpkaboo (Large Size)") in i["ï»¿#"]:
                pokemon_name.append("Pumpkaboo " + pokedex[index + 1]["Name"])

            elif ("Pumpkaboo (Super Size)") in i["ï»¿#"]:
                pokemon_name.append("Pumpkaboo " + pokedex[index + 1]["Name"])

            elif ("Gourgeist (Average Size)") in i["ï»¿#"]:
                pokemon_name.append("Gourgeist " + pokedex[index + 1]["Name"])

            elif ("Gourgeist (Small Size)") in i["ï»¿#"]:
                pokemon_name.append("Gourgeist " + pokedex[index + 1]["Name"])
            
            elif ("Gourgeist (Large Size)") in i["ï»¿#"]:
                pokemon_name.append("Gourgeist " + pokedex[index + 1]["Name"])

            elif ("Gourgeist (Super Size)") in i["ï»¿#"]:
                pokemon_name.append("Gourgeist " + pokedex[index + 1]["Name"])

            elif ("Zygarde (50% Forme)") in i["ï»¿#"]:
                pokemon_name.append("Zygarde " + pokedex[index + 1]["Name"])

            elif ("Zygarde (10% Forme)") in i["ï»¿#"]:
                pokemon_name.append("Zygarde " + pokedex[index + 1]["Name"])

            elif ("Zygarde (Complete Forme)") in i["ï»¿#"]:
                pokemon_name.append("Zygarde " + pokedex[index + 1]["Name"])

            elif ("Oricorio (Baile Style)") in i["ï»¿#"]:
                pokemon_name.append("Oricorio " + pokedex[index + 1]["Name"])

            elif ("Oricorio (Pom-Pom Style)") in i["ï»¿#"]:
                pokemon_name.append("Oricorio " + pokedex[index + 1]["Name"])

            elif ("Oricorio (Pa'u Style)") in i["ï»¿#"]:
                pokemon_name.append("Oricorio " + pokedex[index + 1]["Name"])

            elif ("Oricorio (Sensu Style)") in i["ï»¿#"]:
                pokemon_name.append("Oricorio " + pokedex[index + 1]["Name"])
            
            

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
            

