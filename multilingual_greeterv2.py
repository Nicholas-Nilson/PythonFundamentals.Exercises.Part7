from typing import Dict

# this one might no longer pass the tests originally given, since
# language check no longer returns an integer.
# I wanted a branch to try adding secret options to the user menu, while still retaining all other functionality.
# In this branch an admin can get back to the top menu without restarting the entire app.


# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1: 'English', 2: 'Spanish', 3: 'Japanese', 'Zip Code Rocks': ''}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {1: "What is your name?",
                    2: "¿Cuál es su nombre? (What is your name?)",
                    3: "o namae wa? (What is your name?)"}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {1: "Hello",
                  2: "Hola",
                  3: "こんにちは"}

# Dictionary for program modes
mode_dict = {1: "user", 2: "admin", 3: "turn off"}

# Dictionary for optionals available in admin mode
admin_options_dict = {1: "Add a language", 2: "Change a greeting", 3: "Quit to main menu", 4: "Turn off"}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print("Please choose a language: ")
    for key in lang_options:
        if key == 'Zip Code Rocks':
            continue
        else:
            print("{}: {}".format(key, lang_options[key]))


def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    language_choice = input()
    return language_choice


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    return input_check(lang_options, lang_choice)


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    return name_prompt_options[lang_choice]


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    name = input(name_prompt)
    return name


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    print(greetings_options[lang_choice] + " " + name)


def mode_select_print(mode_options: Dict[int, str]):
    print("Please select mode:")
    for key in mode_options:
        print("{}: {}".format(key, mode_options[key]))


def mode_input():
    mode_choice = input(">>")
    return mode_choice


def input_check(input_dict, input_value):
    try:
        if input_value == 'Zip Code Rocks':
            return input_value in input_dict
        else:
            return int(input_value) in input_dict
    except ValueError:
        return False


def admin_lang_dict_print(language_dict):
    print("Available languages\n")
    code = language_dict.pop('Zip Code Rocks')
    for key in language_dict:
        print("{}: {}".format(key, language_dict[key]))
    language_dict['Zip Code Rocks'] = 'Sure Does'


def admin_actions_print(options_dict):
    print("\nPlease choose an option\n")
    for key in admin_options_dict:
        print("{}: {}".format(key, options_dict[key]))


def admin_add_language_to_dict():
    new_language = input("\nEnter name of language to add\n")
    return new_language


def admin_add_name_prompt(key_to_add,  language_dict):
    new_name_prompt = input("\nPlease enter {} translation for: 'What is your name?'".format(language_dict[key_to_add]))
    return new_name_prompt


def admin_add_greeting(key_to_add, language_dict):
    new_greeting = input("\nPlease enter {} translation for: 'Hello'".format(language_dict[key_to_add]))
    return new_greeting


# this is doing too many things and could be spelled out in main, but it is working. hmmm.
# could split into three adds for easier testing and just call the three in main.
def admin_add_new_language(language_dict, prompt_dict, greeting_dict):
    new_key = len(language_dict)
    admin_lang_dict_print(language_dict)
    language_dict[new_key] = admin_add_language_to_dict()
    name_prompt_dict[new_key] = admin_add_name_prompt(new_key, language_dict)
    greetings_dict[new_key] = admin_add_greeting(new_key, language_dict)


#  -_-
# def admin_update_prompt(key_to_change, prompt_dict, language_dict):
#     prompt_dict[key_to_change] = input(f"\nPlease enter new prompt for {language_dict[key_to_change]}\n")


def admin_update_greeting(key_to_change, greeting_dict, language_dict):
    greeting_dict[key_to_change] = input(f"\nPlease enter new greeting for {language_dict[key_to_change].upper()}\n")


# can use mode_input() here and verify when piecing it all together.
# def admin_input_language_to_change(language_dict):


if __name__ == '__main__':
    # print_language_options(lang_dict)
    # chosen_lang = language_input()
    # while language_choice_is_valid(lang_dict, chosen_lang) is False:
    #     print("Invalid selection. Try again.")
    #     chosen_lang = language_input()
    # selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    # chosen_name = name_input(selected_prompt)
    # greet(chosen_name, greetings_dict, chosen_lang)

    # admin_add_new_language(lang_dict)
    # admin_add_greeting(admin_add_name_prompt(name_prompt_dict, admin_add_language_to_dict(lang_dict), lang_dict), greetings_dict, lang_dict)
    # print(greetings_dict)

    # mode_select_print(mode_dict)
    # mode = mode_input()
    # while language_choice_is_valid(mode_dict, mode) is False:
    #     print("Invalid selection, please try again")
    #     mode = mode_input()
    #
    # admin_add_new_language(lang_dict, name_prompt_dict, greetings_dict)
    # print(lang_dict)
    # print(name_prompt_dict)
    # print(greetings_dict)
    on = True
    while on:
        mode_select_print(mode_dict)
        mode = mode_input()
        while input_check(mode_dict, mode) is False:
            print("Invalid selection. Please choose from available options")
            mode = mode_input()
        while int(mode) == 1:
            print_language_options(lang_dict)
            chosen_lang = language_input()
            while language_choice_is_valid(lang_dict, chosen_lang) is False:
                print("Invalid selection. Try again.")
                chosen_lang = language_input()
            if chosen_lang == 'Zip Code Rocks':
                break
            chosen_lang = int(chosen_lang)
            selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
            chosen_name = name_input(selected_prompt)
            greet(chosen_name, greetings_dict, chosen_lang)
            print("\n")
        while int(mode) == 2:
            admin_lang_dict_print(lang_dict)
            admin_actions_print(admin_options_dict)
            action = mode_input()
            while input_check(admin_options_dict, action) is False:
                print("Invalid selection. Try again.")
                action = mode_input()
            if int(action) == 1:
                admin_add_new_language(lang_dict, name_prompt_dict, greetings_dict)
                added_key = len(lang_dict) - 1
                print("{:<20} {}".format("Added Language:", lang_dict[added_key]))
                print("{:<20} {}".format("Name Prompt:", name_prompt_dict[added_key]))
                print("{:<20} {}\n".format("Greeting", greetings_dict[added_key]))
            elif int(action) == 2:
                admin_lang_dict_print(lang_dict)
                key_to_change = mode_input()
                while input_check(lang_dict, key_to_change) is False:
                    print("Invalid selection. Try again.")
                    key_to_change = mode_input()
                key_to_change = int(key_to_change)
                admin_update_greeting(key_to_change, greetings_dict, lang_dict)
                print("{:<20}: {}".format("Updated Language", lang_dict[key_to_change]))
                print("{:<20}: {}\n".format("New Greeting", greetings_dict[key_to_change]))
            elif int(action) == 3:
                print("Returning to main menu.")
                break
            elif int(action) == 4:
                on = False
                print("Goodbye")
                break
        if int(mode) == 3:
            on = False
            print("Goodbye")

    # admin_update_prompt(1, name_prompt_dict, lang_dict)
    # print(name_prompt_dict)
