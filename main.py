from data import pokedex

#interface class
class Interface:
    next_menu = None
    choice = None
    pokemons = None
    pokemon_types = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dark", "dragon", "steel", "fairy"]
    pokemon_stats_types = ["total", "hp", "attack", "defense", "sp. atk", "sp. def", "speed"]
    retrieving_pokemon_stats_value = False
    sorted_by_type = False
    sorted_by_stats = False

    def __init__(self):
        self.current_menu = MenuDisplay()
    
    #prints logo
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
    
    #prints a text encapsulated in a box
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

    #prompts the user for a choice; returns choice
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

    #prints error message
    def error_message(self, int_error=False, option_error=False):

        if int_error == True:
            Interface.text_box(Interface, "INPUT MUST BE A NUMBER")
            
        elif option_error == True:
            Interface.text_box(Interface, "OPTION NOT AVAILABLE")

        Interface.choice = None
        
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

    #checks if a pokemon type exist
    def if_pokemon_type_exist(self, input_text):
        if input_text.lower() in Interface.pokemon_types: 
            return True
        else:
            return False


    #checks if input is relatively close to a data from a given list; returns the data relatively closest to the input
    def if_text_close_to_pokemon_type(self, input_text, from_list):
        index = 0
        match_count = 0
        index_2 = 0
        match_count_2 = 0
        index_3 = 0
        letter_index = 0
        match_count_3 = 0
        for types in from_list:
            for letter in types:

                if letter == input_text[index]:
                    match_count += 1
                    if index+1 < len(input_text):
                        index += 1
                
                if letter == input_text[index_2]:
                    match_count_2 += 1
                    if index_2+1 < len(input_text):
                        index_2 += 1
                else:
                    if index_2+1 < len(input_text):
                        index_2 += 1

                if types[letter_index] == input_text[index_3]:
                    match_count_3 += 1
                    if index_3+1 < len(input_text):
                        index_3 += 1
                    if letter_index+1 < len(types):
                        letter_index += 1
                else:
                    if index_3+1 < len(input_text):
                        index_3 += 1

                if match_count >= len(types) * 0.6:
                    self.text_box(f"DID YOU MEAN {types.upper()}?")
                    Interface.choice = types
                    return types

                elif match_count_2 >= len(types) * 0.6:
                    self.text_box(f"DID YOU MEAN {types.upper()}?")
                    Interface.choice = types
                    return types

                elif match_count_3 >= len(types) * 0.6:
                    self.text_box(f"DID YOU MEAN {types.upper()}?")
                    Interface.choice = types
                    return types

            index = 0
            match_count = 0
            index_2 = 0
            match_count_2 = 0
            index_3 = 0
            letter_index = 0
            match_count_3 = 0

        return False

    #if input is relatively close to any of the data from the given list returns the relatively closest data from the list
    def auto_complete(self, input_text, from_list):
        for types in from_list:
            if types.startswith(input_text.lower()):
                self.text_box(f"DID YOU MEAN {types.upper()}?")
                Interface.choice = types
                return types
            
            elif self.if_text_close_to_pokemon_type(input_text, from_list) != False:
                break
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
    
    #checks if a pokemon stats type exist
    def if_pokemon_stats_type_exist(self, text_input):
        if text_input.lower() in Interface.pokemon_stats_types:
            return True
        else:
            return False
       
#Prompts the option to display all pokemons or all pokemons by starting letter
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

#Prompts the option to select sorting criteria
class MenuSortSelect(Interface):

    def __init__(self):
        pass

    def prompt_choice(self):
        if Interface.sorted_by_type == True and Interface.sorted_by_stats == True:
            Interface.next_menu = MenuDisplay()
            user_interface.current_menu = Interface.next_menu

        elif Interface.sorted_by_type == True and Interface.sorted_by_stats == False:
            super().prompt_choice("ENTER '1' TO SORT BY STATS, ENTER '2' TO CLEAR LIST")
            if Interface.choice == 1:
                Interface.choice = None
                Interface.next_menu = MenuStatTypeSelect()
                user_interface.current_menu = Interface.next_menu
            elif Interface.choice == 2:
                Interface.choice = None
                Interface.next_menu = MenuDisplay()
                user_interface.current_menu = Interface.next_menu
            else:
                pass
        
        elif Interface.sorted_by_stats == True and Interface.sorted_by_type == False :
            super().prompt_choice("ENTER '1' TO SORT BY TYPE, ENTER '2' TO CLEAR LIST")
            if Interface.choice == 1:
                Interface.choice = None
                Interface.next_menu = MenuTypeSelect()
                user_interface.current_menu = Interface.next_menu
            elif Interface.choice == 2:
                Interface.choice = None
                Interface.next_menu = MenuDisplay()
                user_interface.current_menu = Interface.next_menu
            else:
                pass

        else:  
            super().prompt_choice("ENTER '1' TO SORT BY TYPE, ENTER '2' TO SORT BY STATS")
        
    def option_1(self):
        Interface.next_menu = MenuTypeSelect()
    
    def option_2(self):
        Interface.next_menu = MenuStatTypeSelect()

#Prompts the option to select pokemon stats type
class MenuStatTypeSelect(Interface):
    stat_type = None

    def __init__(self):
        pass
    
    def prompt_choice(self):
        Interface.sorted_by_stats = True
        super().prompt_choice("ENTER '1' TO SELECT STAT TYPE, ENTER '2' TO SEE ALL STAT TYPES")
        if Interface.choice == 1:
            MenuStatTypeSelect.stat_type = super().prompt_choice("ENTER STAT TYPE", str=True)
            if self.if_pokemon_stats_type_exist(MenuStatTypeSelect.stat_type):
                Interface.next_menu = MenuStatValueSelect()
                user_interface.current_menu = Interface.next_menu

            elif self.auto_complete(Interface.choice, Interface.pokemon_stats_types) != False:
                selected_type = Interface.choice
                super().prompt_choice("YES: ENTER '1', NO: ENTER '2'")
                if Interface.choice == 1:
                    Interface.choice = None
                    MenuStatTypeSelect.stat_type = selected_type
                    Interface.next_menu = MenuStatValueSelect()
                    user_interface.current_menu = Interface.next_menu

                elif Interface.choice == 2:
                    Interface.choice = None

            else:
                self.text_box("STAT TYPE DOES NOT EXIST")

        elif Interface.choice == 2:
            Interface.choice = None
            print("")
            for i in Interface.pokemon_stats_types:
                print(i.title())

        else:
            pass

#Prompts the option to enter pokemon stats value
class MenuStatValueSelect(Interface):
    stat_value = None

    def __init__(self):
        pass

    def prompt_choice(self):
        Interface.retrieving_pokemon_stats_value = True
        MenuStatValueSelect.stat_value = super().prompt_choice("ENTER STAT VALUE")
        if type(MenuStatValueSelect.stat_value) == int:
            Interface.choice = None
            Interface.retrieving_pokemon_stats_value = False
            Interface.next_menu = MenuStatSort()
            user_interface.current_menu = Interface.next_menu
        else:
            pass

#Prompt the option to select sorting condition; prints a list of pokemon with the specified stats type, stats value and sorting condition
class MenuStatSort(Interface):

    def __init__(self):
        pass

    def prompt_choice(self):
        self.sort_condition = super().prompt_choice("ENTER '1' TO SORT BY MINIMUM STAT VALUE, ENTER '2' TO SORT BY MAXIMUM STAT VALUE, ENTER '3' TO SORT BY SPECIFIC STAT VALUE")
        
        if self.sort_condition == 1:
            Interface.pokemons = self.pokemon_with_stats(MenuStatTypeSelect.stat_type, MenuStatValueSelect.stat_value, min=True, pokemon_list=Interface.pokemons)
            self.display_pokemon_list(pokemon_list=Interface.pokemons)
            Interface.choice = None
            Interface.next_menu = MenuSortSelect()
            user_interface.current_menu = Interface.next_menu

        elif self.sort_condition == 2:
            Interface.pokemons = self.pokemon_with_stats(MenuStatTypeSelect.stat_type, MenuStatValueSelect.stat_value, max=True, pokemon_list=Interface.pokemons)
            self.display_pokemon_list(pokemon_list=Interface.pokemons)
            Interface.choice = None
            Interface.next_menu = MenuSortSelect()
            user_interface.current_menu = Interface.next_menu

        elif self.sort_condition == 3:
            Interface.pokemons = self.pokemon_with_stats(MenuStatTypeSelect.stat_type, MenuStatValueSelect.stat_value, pokemon_list=Interface.pokemons)
            self.display_pokemon_list(pokemon_list=Interface.pokemons)
            Interface.choice = None
            Interface.next_menu = MenuSortSelect()
            user_interface.current_menu = Interface.next_menu

        else:
            pass

#Prompts the option to select pokemon type sorting criteria
class MenuTypeSelect(Interface):
    sort_selection = None

    def __init__(self):
        pass

    def prompt_choice(self):
        Interface.sorted_by_type = True
        super().prompt_choice("ENTER '1' TO SORT ALL POKEMON WITH THE SPECIFIED TYPE, ENTER '2' TO SORT ALL POKEMON WITH ONLY THE SPECIFIED TYPE, ENTER '3' TO SEE ALL POKEMON TYPES")

    def option_1(self):
        Interface.next_menu = MenuSortAnyTypeSelect()

    def option_2(self):
        MenuTypeSelect.sort_selection = 'sort by only type'
        Interface.next_menu = MenuTypeSort()

    def option_3(self):
        print("")
        for i in Interface.pokemon_types:
            print(i.title())

#Prompts the option to select to sort between 1 type or 2 types
class MenuSortAnyTypeSelect(MenuTypeSelect):

    def prompt_choice(self):
        Interface.prompt_choice(self, "ENTER '1' TO SORT BY ONE TYPE, ENTER '2' TO SORT BY TWO TYPES, ENTER '3' TO SEE ALL POKEMON TYPES")

    def option_1(self):
        MenuTypeSelect.sort_selection = 'sort by one type'
        Interface.next_menu = MenuTypeSort()

    def option_2(self):
        MenuTypeSelect.sort_selection = 'sort by two types'
        Interface.next_menu = MenuTypeSort()

#Prompts the option to enter pokemon types/type, depending on the sorting criteria; prints a sorted pokemon list
class MenuTypeSort(Interface):

    def __init__(self):
        pass

    def prompt_choice(self):
        if MenuTypeSelect.sort_selection == 'sort by one type':
            pokemon_type = []
            super().prompt_choice("ENTER TYPE", str=True)
            if self.if_pokemon_type_exist(Interface.choice):
                pokemon_type.append(Interface.choice)
                Interface.pokemons = self.pokemon_with_type(pokemon_type, pokemon_list=Interface.pokemons)
                self.display_pokemon_list(pokemon_list=Interface.pokemons)
                Interface.next_menu = MenuSortSelect()
                user_interface.current_menu = Interface.next_menu

            elif self.auto_complete(Interface.choice, Interface.pokemon_types) != False:
                selected_type = Interface.choice
                super().prompt_choice("YES: ENTER '1', NO: ENTER '2'")
                if Interface.choice == 1:
                    Interface.choice = None
                    pokemon_type.append(selected_type)
                    Interface.pokemons = self.pokemon_with_type(pokemon_type, pokemon_list=Interface.pokemons)
                    self.display_pokemon_list(pokemon_list=Interface.pokemons)
                    Interface.next_menu = MenuSortSelect()
                    user_interface.current_menu = Interface.next_menu

                elif Interface.choice == 2:
                    Interface.choice = None

            else:
                self.text_box("TYPE DOES NOT EXIST")

        if MenuTypeSelect.sort_selection == 'sort by two types':
            second_type_valid = False
            pokemon_type = []
            super().prompt_choice("ENTER TYPE", str=True)
            if self.if_pokemon_type_exist(Interface.choice):
                pokemon_type.append(Interface.choice)
                while second_type_valid == False:
                    super().prompt_choice("ENTER SECOND TYPE", str=True)
                    if self.if_pokemon_type_exist(Interface.choice):
                        second_type_valid = True
                        pokemon_type.append(Interface.choice)
                        Interface.pokemons = self.pokemon_with_type(pokemon_type, pokemon_list=Interface.pokemons)
                        self.display_pokemon_list(pokemon_list=Interface.pokemons)
                        Interface.next_menu = MenuSortSelect()
                        user_interface.current_menu = Interface.next_menu
                    else:
                        self.text_box("TYPE DOES NOT EXIST")

            elif self.auto_complete(Interface.choice, Interface.pokemon_types) != False:
                selected_type = Interface.choice
                super().prompt_choice("YES: ENTER '1', NO: ENTER '2'")
                if Interface.choice == 1:
                    Interface.choice = None
                    pokemon_type.append(selected_type)
                    while second_type_valid == False:
                        super().prompt_choice("ENTER SECOND TYPE", str=True)
                        if self.if_pokemon_type_exist(Interface.choice):
                            second_type_valid = True
                            pokemon_type.append(Interface.choice)
                            Interface.pokemons = self.pokemon_with_type(pokemon_type, pokemon_list=Interface.pokemons)
                            self.display_pokemon_list(pokemon_list=Interface.pokemons)
                            Interface.next_menu = MenuSortSelect()
                            user_interface.current_menu = Interface.next_menu

                        elif self.auto_complete(Interface.choice, Interface.pokemon_types) != False:
                            selected_type = Interface.choice
                            super().prompt_choice("YES: ENTER '1', NO: ENTER '2'")
                            if Interface.choice == 1:
                                second_type_valid = True
                                Interface.choice = None
                                pokemon_type.append(selected_type)
                                Interface.pokemons = self.pokemon_with_type(pokemon_type, pokemon_list=Interface.pokemons)
                                self.display_pokemon_list(pokemon_list=Interface.pokemons)
                                Interface.next_menu = MenuSortSelect()
                                user_interface.current_menu = Interface.next_menu

                            elif Interface.choice == 2:
                                Interface.choice = None

                        else:
                            self.text_box("TYPE DOES NOT EXIST")

                elif Interface.choice == 2:
                    Interface.choice = None

            else:
                self.text_box("TYPE DOES NOT EXIST")

        if MenuTypeSelect.sort_selection == 'sort by only type':
            pokemon_type = []
            super().prompt_choice("ENTER TYPE", str=True)
            if self.if_pokemon_type_exist(Interface.choice):
                pokemon_type.append(Interface.choice)
                Interface.pokemons = self.pokemon_with_type(pokemon_type, only_type=True, pokemon_list=Interface.pokemons)
                self.display_pokemon_list(pokemon_list=Interface.pokemons)
                Interface.next_menu = MenuSortSelect()
                user_interface.current_menu = Interface.next_menu

            elif self.auto_complete(Interface.choice, Interface.pokemon_types) != False:
                selected_type = Interface.choice
                super().prompt_choice("YES: ENTER '1', NO: ENTER '2'")
                if Interface.choice == 1:
                    Interface.choice = None
                    pokemon_type.append(selected_type)
                    Interface.pokemons = self.pokemon_with_type(pokemon_type, only_type=True, pokemon_list=Interface.pokemons)
                    self.display_pokemon_list(pokemon_list=Interface.pokemons)
                    Interface.next_menu = MenuSortSelect()
                    user_interface.current_menu = Interface.next_menu

                if Interface.choice == 2:
                    Interface.choice = None

            else:
                self.text_box("TYPE DOES NOT EXIST")

#Instantiate
user_interface = Interface()
user_interface.logo()

#Start
while True:

    user_interface.current_menu.prompt_choice()

    try:
        if Interface.choice == 1:
            user_interface.current_menu.option_1()
            user_interface.current_menu = Interface.next_menu
            Interface.choice = None
        
        elif Interface.choice == 2:
            user_interface.current_menu.option_2()
            user_interface.current_menu = Interface.next_menu
            Interface.choice = None

        elif Interface.choice == 3:
            user_interface.current_menu.option_3()
            user_interface.current_menu = Interface.next_menu
            Interface.choice = None

        else:
            if type(Interface.choice) == int:

                if Interface.retrieving_pokemon_stats_value == True:
                    pass
                
                else:
                    Interface.error_message(Interface, option_error=True)
    except AttributeError:
        Interface.error_message(Interface, option_error=True)