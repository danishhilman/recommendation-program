from data import pokedex

#interface class
class Interface:
    next_menu = None
    choice = None
    pokemons = None
    pokemon_types = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dark", "Dragon", "Steel", "Fairy"]
    pokemon_stats_types = ["Total", "Hp", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
    retrieving_pokemon_stats_value = False
    sorted_by_type = False
    sorted_by_stats = False

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

    def prompt_choice(self, text=None, str=False):
        self.text_box(text)
        print("\n", "= ", end="")
        if str == False:
            try:
                Interface.choice = int(input())
            except:
                self.error_message(int_error=True)

        if str == True:
            Interface.choice = input()

        return Interface.choice

    def error_message(self, int_error=False, option_error=False, pokemon_type_error=False):

        if int_error == True:
            self.text_box("INPUT MUST BE A NUMBER")
            
        elif option_error == True:
            Interface.text_box(Interface, "OPTION NOT AVAILABLE")
        
        elif pokemon_type_error == True:
            self.text_box("TYPE DOES NOT EXIST")
    
    #prints all pokemon mapped to their respective type and stats
    def display_pokemon_list(self, pokemon_list=pokedex):
        print("")
        if len(pokemon_list) == 0:
            print("NO POKEMON FOUND")
        else:
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

    def if_pokemon_type_exist(self, input):
        if input in Interface.pokemon_types: 
            return True
        else:
            return False

    #returns a dictionary of all the pokemon with a specified stats category with a maximum value, minimum value or specific value
    def pokemon_with_stats(self, stat_type, val, min=False, max=False, pokemon_list=pokedex):

        stat_type = stat_type.title()
        if stat_type == "Hp":
            stat_type = stat_type.upper()
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
    
    def if_pokemon_stats_type_exist(self, input):
        if input in Interface.pokemon_stats_types:
            return True
        else:
            return False
       
       
#First Menu/Page
class MenuDisplay(Interface):

    def __init__(self):
        pass

    def prompt_choice(self):
        Interface.sorted_by_type = False
        Interface.sorted_by_stats = False
        super().prompt_choice("TO DISPLAY ALL POKEMON ENTER '1', TO SEARCH POKEMON BY NAME OR FIRST LETTER ENTER '2'")
        
    def option_1(self):
        Interface.next_menu = MenuSortSelect()
        Interface.pokemons = pokedex
        self.display_pokemon_list(pokemon_list=Interface.pokemons)

    def option_2(self):
        Interface.next_menu = MenuSortSelect()
        super().prompt_choice("ENTER THE POKEMON'S STARTING LETTER OR NAME", str=True)
        Interface.pokemons = self.pokemon_by_starting_letter(Interface.choice)
        self.display_pokemon_list(pokemon_list=Interface.pokemons)

class MenuSortSelect(Interface):

    def __init__(self):
        pass

    def prompt_choice(self):
        if Interface.sorted_by_type == True and Interface.sorted_by_stats == True:
            Interface.next_menu = MenuDisplay()
            interface.current_menu = Interface.next_menu

        elif Interface.sorted_by_type == True and Interface.sorted_by_stats == False:
            super().prompt_choice("ENTER '1' TO SORT BY STATS, ENTER '2' TO CLEAR LIST")
            if Interface.choice == 1:
                Interface.choice = None
                Interface.next_menu = MenuStatTypeSelect()
                interface.current_menu = Interface.next_menu
            
            elif Interface.choice == 2:
                Interface.choice = None
                Interface.next_menu = MenuDisplay()
                interface.current_menu = Interface.next_menu
            
            else:
                pass
        
        elif Interface.sorted_by_stats == True and Interface.sorted_by_type == False :
            super().prompt_choice("ENTER '1' TO SORT BY TYPE, ENTER '2' TO CLEAR LIST")
            if Interface.choice == 1:
                Interface.choice = None
                Interface.next_menu = MenuTypeSelect()
                interface.current_menu = Interface.next_menu

            elif Interface.choice == 2:
                Interface.choice = None
                Interface.next_menu = MenuDisplay()
                interface.current_menu = Interface.next_menu

            else:
                pass
        else:  
            super().prompt_choice("ENTER '1' TO SORT BY TYPE, ENTER '2' TO SORT BY STATS")
        
    def option_1(self):
        Interface.next_menu = MenuTypeSelect()
    
    def option_2(self):
        Interface.next_menu = MenuStatTypeSelect()

class MenuStatTypeSelect(Interface):
    stat_type = None
    def prompt_choice(self):
        Interface.sorted_by_stats = True
        MenuStatTypeSelect.stat_type = super().prompt_choice("ENTER STAT TYPE", str=True)
        if self.if_pokemon_stats_type_exist(MenuStatTypeSelect.stat_type.title()):
            Interface.next_menu = MenuStatValueSelect()
            interface.current_menu = Interface.next_menu
        else:
            self.text_box("STAT TYPE DOES NOT EXIST")

class MenuStatValueSelect(Interface):
    stat_value = None
    def prompt_choice(self):
        Interface.retrieving_pokemon_stats_value = True
        MenuStatValueSelect.stat_value = super().prompt_choice("ENTER STAT VALUE")
        if type(MenuStatValueSelect.stat_value) == int:
            Interface.choice = None
            Interface.retrieving_pokemon_stats_value = False
            Interface.next_menu = MenuStatSort()
            interface.current_menu = Interface.next_menu
        else:
            pass

class MenuStatSort(Interface):

    def prompt_choice(self):
        self.sort_condition = super().prompt_choice("ENTER '1' TO SORT BY MINIMUM STAT VALUE, ENTER '2' TO SORT BY MAXIMUM STAT VALUE, ENTER '3' TO SORT BY SPECIFIC STAT VALUE")
        
        if self.sort_condition == 1:
            Interface.pokemons = self.pokemon_with_stats(MenuStatTypeSelect.stat_type, MenuStatValueSelect.stat_value, min=True, pokemon_list=Interface.pokemons)
            self.display_pokemon_list(pokemon_list=Interface.pokemons)
            Interface.choice = None
            Interface.next_menu = MenuSortSelect()
            interface.current_menu = Interface.next_menu

        elif self.sort_condition == 2:
            Interface.pokemons = self.pokemon_with_stats(MenuStatTypeSelect.stat_type, MenuStatValueSelect.stat_value, max=True, pokemon_list=Interface.pokemons)
            self.display_pokemon_list(pokemon_list=Interface.pokemons)
            Interface.choice = None
            Interface.next_menu = MenuSortSelect()
            interface.current_menu = Interface.next_menu

        elif self.sort_condition == 3:
            Interface.pokemons = self.pokemon_with_stats(MenuStatTypeSelect.stat_type, MenuStatValueSelect.stat_value, pokemon_list=Interface.pokemons)
            self.display_pokemon_list(pokemon_list=Interface.pokemons)
            Interface.choice = None
            Interface.next_menu = MenuSortSelect()
            interface.current_menu = Interface.next_menu

        else:
            pass

class MenuTypeSelect(MenuSortSelect):
    sort_selection = None

    def __init__(self):
        pass

    def prompt_choice(self):
        Interface.sorted_by_type = True
        Interface.prompt_choice(self, "ENTER '1' TO SORT ALL POKEMON WITH THE SPECIFIED TYPE, ENTER '2' TO SORT ALL POKEMON WITH ONLY THE SPECIFIED TYPE")

    def option_1(self):
        Interface.next_menu = MenuSortAnyTypeSelect()

    def option_2(self):
        MenuTypeSelect.sort_selection = 'sort by only type'
        Interface.next_menu = MenuTypeSort()

class MenuSortAnyTypeSelect(MenuTypeSelect):

    def prompt_choice(self):
        Interface.prompt_choice(self, "ENTER '1' TO SORT BY ONE TYPE, ENTER '2' TO SORT BY TWO TYPES")

    def option_1(self):
        MenuTypeSelect.sort_selection = 'sort by one type'
        Interface.next_menu = MenuTypeSort()

    def option_2(self):
        MenuTypeSelect.sort_selection = 'sort by two types'
        Interface.next_menu = MenuTypeSort()

class MenuTypeSort(Interface):

    def prompt_choice(self):
        if MenuTypeSelect.sort_selection == 'sort by one type':
            pokemon_type = []
            super().prompt_choice("ENTER TYPE", str=True)
            if self.if_pokemon_type_exist(Interface.choice.title()):
                pokemon_type.append(Interface.choice)
                Interface.pokemons = self.pokemon_with_type(pokemon_type, pokemon_list=Interface.pokemons)
                self.display_pokemon_list(pokemon_list=Interface.pokemons)
                Interface.next_menu = MenuSortSelect()
                interface.current_menu = Interface.next_menu
            else:
                self.text_box("TYPE DOES NOT EXIST")

        if MenuTypeSelect.sort_selection == 'sort by two types':
            second_type_valid = False
            pokemon_type = []
            super().prompt_choice("ENTER TYPE", str=True)
            if self.if_pokemon_type_exist(Interface.choice.title()):
                pokemon_type.append(Interface.choice)
                while second_type_valid == False:
                    super().prompt_choice("ENTER SECOND TYPE", str=True)
                    if self.if_pokemon_type_exist(Interface.choice.title()):
                        second_type_valid = True
                        pokemon_type.append(Interface.choice)
                        Interface.pokemons = self.pokemon_with_type(pokemon_type, pokemon_list=Interface.pokemons)
                        self.display_pokemon_list(pokemon_list=Interface.pokemons)
                        Interface.next_menu = MenuSortSelect()
                        interface.current_menu = Interface.next_menu
                    else:
                        self.text_box("TYPE DOES NOT EXIST")
            else:
                self.text_box("TYPE DOES NOT EXIST")

        if MenuTypeSelect.sort_selection == 'sort by only type':
            pokemon_type = []
            super().prompt_choice("ENTER TYPE", str=True)
            if self.if_pokemon_type_exist(Interface.choice.title()):
                pokemon_type.append(Interface.choice)
                Interface.pokemons = self.pokemon_with_type(pokemon_type, only_type=True, pokemon_list=Interface.pokemons)
                self.display_pokemon_list(pokemon_list=Interface.pokemons)
                Interface.next_menu = MenuSortSelect()
                interface.current_menu = Interface.next_menu
            else:
                self.text_box("TYPE DOES NOT EXIST")

#Instantiate
interface = Interface()
interface.logo()

#Interface Start
while True:

    interface.current_menu.prompt_choice()

    if Interface.choice == 1:
        interface.current_menu.option_1()
        interface.current_menu = Interface.next_menu
        Interface.choice = None
    
    elif Interface.choice == 2:
        interface.current_menu.option_2()
        interface.current_menu = Interface.next_menu
        Interface.choice = None

    else:
        if type(Interface.choice) == int:

            if Interface.retrieving_pokemon_stats_value == True:
                pass
            
            else:
                Interface.error_message(Interface, option_error=True)