from data import pokedex

#interface class
class Interface:
    next_menu = None
    choice = 0
    pokemons = None

    def __init__(self):
        self.current_menu = MenuDisplay()
        
    def logo(self):
        print(""" .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |   ______     | | |     ____     | | |  ___  ____   | | |  _________   | | |  ________    | | |  _________   | | |  ____  ____  | |
| |  |_   __ \   | | |   .'    `.   | | | |_  ||_  _|  | | | |_   ___  |  | | | |_   ___ `.  | | | |_   ___  |  | | | |_  _||_  _| | |
| |    | |__) |  | | |  /  .--.  \  | | |   | |_/ /    | | |   | |_  \_|  | | |   | |   `. \ | | |   | |_  \_|  | | |   \ \  / /   | |
| |    |  ___/   | | |  | |    | |  | | |   |  __'.    | | |   |  _|  _   | | |   | |    | | | | |   |  _|  _   | | |    > `' <    | |
| |   _| |_      | | |  \  `--'  /  | | |  _| |  \ \_  | | |  _| |___/ |  | | |  _| |___.' / | | |  _| |___/ |  | | |  _/ /'`\ \_  | |
| |  |_____|     | | |   `.____.'   | | | |____||____| | | | |_________|  | | | |________.'  | | | |_________|  | | | |____||____| | |
| |              | | |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' """)

    def text_box(self, text):
        print(" ", end="")
        for i in range(len(text)+2):
            print("_", end="")
        else:
            print("\n", end="")

        print("|", end="")

        for i in range(len(text)+2):
            print(" ",end="")
        else:
            print("|")
    
        print("|", text, "|")

        print("|", end="")
        for i in range(len(text)+2):
            print("_", end="")
        else:
            print("|")

    def prompt_choice(self, text=None, str =False):
        self.text_box(text)
        print("\n", end="")
        print("= ", end="")
        if str == False:
            Interface.choice = int(input())
        if str == True:
            Interface.choice = input()
        print("\n")
        return Interface.choice

    #prints all pokemon mapped to their respective type and stats
    def display_pokemon_list(self, pokemon_list=pokedex):
        for i in pokemon_list:
            print("{pokemon}\n Type: {type}\n Stats: {stats}\n".format(pokemon=i, type=pokemon_list[i]["Type"], stats=pokemon_list[i]["Stats"]))

    #if a pokemon name starts with the specified letter/word; returns a dictionary with the pokemon mapped to their respective type and stats
    def pokemon_by_starting_letter(self, letter, pokemon_list=pokedex):
        sorted_pokemon = {}
        for i in sorted(pokemon_list):
            if i.startswith(str(letter).title()):
                sorted_pokemon[i] = {"Type":pokemon_list[i]["Type"], "Stats":pokemon_list[i]["Stats"]}
        return sorted_pokemon

    #returns a dictionary of all the pokemon which has the specified type OR returns a list of all pokemon with only the specified type
    def pokemon_with_type(self, type, only_type=False, pokemon_list=pokedex):
        sorted_pokemon = {}
        type = [x.upper() for x in type]
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
    def pokemon_with_stats(self, stat_type, val, min=False, max=False, pokemon_list=pokedex):
        stat_type = stat_type.title()
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
       
       
#First Menu/Page
class MenuDisplay(Interface):

    def __init__(self):
        pass

    def prompt_choice(self):
        super().prompt_choice("TO DISPLAY ALL POKEMON ENTER '1', TO SEARCH POKEMON BY NAME OR FIRST LETTER ENTER '2'")
        
    def option_1(self):
        Interface.next_menu = MenuSortByTypeOrStats()
        Interface.pokemons = pokedex
        self.display_pokemon_list(pokemon_list=Interface.pokemons)

    def option_2(self):
        Interface.next_menu = MenuSortByTypeOrStats()
        super().prompt_choice("ENTER THE POKEMON'S STARTING LETTER OR NAME", str=True)
        Interface.pokemons = self.pokemon_by_starting_letter(Interface.choice)
        self.display_pokemon_list(pokemon_list=Interface.pokemons)

class MenuSortByTypeOrStats(Interface):

    def __init__(self):
        pass

    def prompt_choice(self):
         super().prompt_choice("ENTER '1' TO SORT BY TYPE, ENTER '2' TO SORT BY STATS")

    def option_1(self):
        Interface.next_menu = MenuSortByStats()
        super().prompt_choice("ENTER '1' TO SORT ALL POKEMON WITH THE SPECIFIED TYPE, ENTER '2' TO SORT ALL POKEMON WITH ONLY THE SPECIFIED TYPE")
        type = []
        if Interface.choice == 1:
            super().prompt_choice("ENTER '1' TO SORT BY ONE TYPE, ENTER '2' TO SORT BY TWO TYPES")
            if Interface.choice == 1:
                type.append(super().prompt_choice("ENTER TYPE", str=True))
                Interface.pokemons = self.pokemon_with_type(type, pokemon_list=Interface.pokemons)
                self.display_pokemon_list(pokemon_list=Interface.pokemons)
            elif Interface.choice == 2:
                type.append(super().prompt_choice("ENTER FIRST TYPE", str=True))
                type.append(super().prompt_choice("ENTER SECOND TYPE", str=True))
                Interface.pokemons = self.pokemon_with_type(type, pokemon_list=Interface.pokemons)
                self.display_pokemon_list(pokemon_list=Interface.pokemons)
            
        elif Interface.choice == 2:
            type.append(super().prompt_choice("ENTER POKEMON TYPE", str=True))
            Interface.pokemons = self.pokemon_with_type(type, only_type=True, pokemon_list=Interface.pokemons)
            self.display_pokemon_list(pokemon_list=Interface.pokemons)
            

    def option_2(self):
        Interface.next_menu = MenuSortByType()
        sort_condition = super().prompt_choice("ENTER '1' TO SORT BY MINIMUM STAT VALUE, ENTER '2' TO SORT BY MAXIMUM STAT VALUE, ENTER '3' TO SORT BY SPECIFIC STAT VALUE")
        stat_type = super().prompt_choice("ENTER STAT TYPE", str=True)
        stat_value = super().prompt_choice("ENTER STAT VALUE")
        
        if sort_condition == 1:
            Interface.pokemons = self.pokemon_with_stats(stat_type, stat_value, min=True, pokemon_list=Interface.pokemons)
            self.display_pokemon_list(pokemon_list=Interface.pokemons)

        elif sort_condition == 2:
            Interface.pokemons = self.pokemon_with_stats(stat_type, stat_value, max=True, pokemon_list=Interface.pokemons)
            self.display_pokemon_list(pokemon_list=Interface.pokemons)

        elif sort_condition == 3:
            Interface.pokemons = self.pokemon_with_stats(stat_type, stat_value, pokemon_list=Interface.pokemons)
            self.display_pokemon_list(pokemon_list=Interface.pokemons)

class MenuSortByStats(MenuSortByTypeOrStats):

    def __init__(self):
        pass

    def prompt_choice(self):
        Interface.prompt_choice(self, "ENTER '1' TO SORT BY STATS, ENTER '2' TO CLEAR LIST")

    def option_1(self):
        super().option_2()
        Interface.next_menu = MenuDisplay()
        
    def option_2(self):
        Interface.next_menu = MenuDisplay()

class MenuSortByType(MenuSortByTypeOrStats):
    
    def __init__(self):
        pass

    def prompt_choice(self):
        Interface.prompt_choice(self, "ENTER '1' TO SORT BY TYPE, ENTER '2' TO CLEAR LIST")

    def option_1(self):
        super().option_1()
        Interface.next_menu = MenuDisplay()

    def option_2(self):
        Interface.next_menu = MenuDisplay()

#Instantiate
interface = Interface()
interface.logo()

#Interface Start
while True:

    interface.current_menu.prompt_choice()

    if Interface.choice == 1:
        interface.current_menu.option_1()
        interface.current_menu = Interface.next_menu
        Interface.choice = 0
    
    elif Interface.choice == 2:
        interface.current_menu.option_2()
        interface.current_menu = Interface.next_menu
        Interface.choice = 0