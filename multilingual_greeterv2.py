from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1: 'English', 2: 'Spanish', 3: 'Japanese'}

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
mode_dict = {1: "user", 2: "admin"}

# Dictionary for optionals available in admin mode
admin_options_dict = {1: "Add a language", 2: "Change a greeting"}


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
        print("{}: {}".format(key, lang_options[key]))


def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    language_choice = input()
    return int(language_choice)


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
    mode_choice = input()
    return int(mode_choice)


def input_check(input_dict, input_value):
    return input_value in input_dict


def admin_lang_dict_print(language_dict):
    print("Available languages\n")
    for key in language_dict:
        print("{}: {}".format(key, language_dict[key]))


def admin_actions_print(options_dict):
    print("\nPlease choose an option\n")
    for key in admin_options_dict:
        print("{}: {}".format(key, options_dict[key]))


def admin_add_language(language_dict):
    new_language = input("\nEnter name of language to add")
    new_key = len(language_dict) + 1
    language_dict[new_key] = new_language
    return new_key


def admin_add_name_prompt(ask_name_dict, key_to_add, language_dict):
    new_name_prompt = input("\nPlease enter {} translation for: 'What is your name?'".format(language_dict[key_to_add]))
    ask_name_dict[key_to_add] = new_name_prompt + " (What is your name?)"



if __name__ == '__main__':
    # print_language_options(lang_dict)
    # chosen_lang = language_input()
    # while language_choice_is_valid(lang_dict, chosen_lang) is False:
    #     print("Invalid selection. Try again.")
    #     chosen_lang = language_input()
    # selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    # chosen_name = name_input(selected_prompt)
    # greet(chosen_name, greetings_dict, chosen_lang)
    admin_lang_dict_print(lang_dict)
    admin_actions_print(admin_options_dict)
    # admin_add_language(lang_dict)
    admin_add_name_prompt(name_prompt_dict, admin_add_language(lang_dict), lang_dict)
    print(name_prompt_dict)