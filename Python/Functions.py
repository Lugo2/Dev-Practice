# Example function:
def display_name(name):
    print(name)
    #  this is the logic of the function

# The above function takes in a variable, known as the parameter.
# In this example, that variable is name.
# The function then prints to the console the value that is passed in


display_name('MarDog')
display_name('VicDog')
display_name('Day Day')

# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 'Mike'

# Example 2


def add_one_to_number(number):
    number_one = 1
    add_one = number + number_one
    return add_one

# The above function takes in a variable, known as the parameter.
# In this example, that variable is number.
# The function then adds one to the parameter and returns the sum


result = add_one_to_number(30)
print(result)


# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 30
# We create and set a variable equal to the function call becuase the function returns a value
# print the result to the terminal

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Task 1, add two numbers
def simple_addition(number_1, number_2):
    e_sum = number_1 + number_2
    return e_sum

print(simple_addition(9, 7))

# user_input_1 = int(input("What's the first number you'd like to add? "))
# user_input_2 = int(input("...and the second? "))                                  <----uncomment to choose 2 numbers to add
# print(simple_addition(user_input_1, user_input_2))



# Task 2, adding two strings
def string_concatenator(string_1, string_2):
    concatenated_statement = string_1 + " " + string_2
    return concatenated_statement

print(string_concatenator("Hello", "world!"))

# user_input_1 = input("What's the first word you'd like to print? ")
# user_input_2 = input("...and the second? ")                                        # <----uncomment to choose 2 words to print
# print(string_concatenator(user_input_1, user_input_2))
    


# Task 3, print string into individual characters on the console
def string_to_letter(string):
    for letter in string:
        print(letter)

string = input("Give me a word to turn into individual letters: ")
string_to_letter(string)



# Task 4, print word to console only if >= 3
def print_if_greater_than_or_equal_to_3(string):
    string_length = len(string)
    if string_length >= 3:
        print(string)
    else:
        print("We need a larger word to print!")

print_if_greater_than_or_equal_to_3("Lol")



# Task 5, function that takes first and last letter of a word and prints them to a console
    # Steps to solve this challenge:
        # 1}    define a function that will take in a string as an argument
        # 2}    find out how to capture the first and last character of a word into two seprate
        #       variables using, loops, conditionals, lists (no built-in List methods), and functions
        # 3}    print the two variables concatenated
def first_letter_extractor(string):
    for first_letter in string:
        return first_letter
        
def last_letter_extractor(string):
    backwards_string = string[::-1]
    for last_letter in backwards_string:
        return last_letter

def first_and_last_letters(string):
    return_first_letter = first_letter_extractor(string)
    return_last_letter = last_letter_extractor(string)
    front_and_last = return_first_letter + return_last_letter
    return front_and_last

string = input("Im going to give you back the first and last letters of what ever word you give me.\nWhat word would you like those two letters to come from? ")
print(first_and_last_letters(string))



# Task 6, function that prints every number from 0 to 100 and prints "peanut butter" if the number is divisable by 3, 
    #     "jelly" if divisible by 5, and "peanutbutter & jelly when divisable by 3 and 5.
    # Steps to solve this challange:
        # 1}    define a function that uses a for loop to print a range of 0 to 100
        # 2}    create conditionals in the function that print "peanut butter" 
        #       "jelly" "peanutbutter & jelly" or a number depending on if a 
        #       condition is met
        # 3}    return the result
        # 4}    print to console
def number_or_peanutbutter_and_jelly():
    for number in range(100):
        if number % 3 == 0 and number % 5 == 0:
            print("peanut butter & jelly")
        elif number % 3 == 0:
             print("peanut butter")
        elif number % 5 == 0:
            print("jelly")
        else:
            print(number)

number_or_peanutbutter_and_jelly()



# Task 7, function that indexes an input word
    # Steps to solve this challenge:
        # 1}    define a function that takes in a string
        # 2}    assign an empty string to a variable
        # 3}    create a loop that concatenates the index of a character in the string , after the string
        # 4}    return concatenated string
        # 4}    print the new value of the variable by calling the function
def word_to_index(string):
    final_result = ""
    length_of_string = len(string)
    eterations = 0
    for character in string:
        index = string.index(character)
        if index != eterations:
            index = eterations
        index_number = str(index)
        index += 1
        indexed_character = character + index_number
        final_result += indexed_character
        eterations += 1
        if eterations == length_of_string:
            return final_result
    
print(word_to_index("sleep sheep"))



# Task 8, write a function that checks for an indredient from list called "ingredients" and returns an ingredient if it exists in the list and a message if not
    # Steps to solve this challenge:
        # 1}    define a function that takes in a list
        # 2}    declare a variable prompting the user for an ingredient to search for
        # 3}    check the list parameter(igredientS) for the element(ingredient) from the user input
        # 4}    if ingredient element is present in the ingredients list parameter, return the ingredient as a string
        # 5}    if ingredient element isn't present in the ingredients list parameter, ask the user if they want to search for another ingredient
def ingredient_finder(list):
    ingredient_to_authenticate = input("What ingredient would you like to check for in the list? ")
    ingredient_in_list = False
    while ingredient_in_list != True:
        if ingredient_to_authenticate in list:
            ingredient_in_list = True
            ingredient_confirmed = f"\n{ingredient_to_authenticate} is on the list!"
            return ingredient_confirmed
        else:
            try_again = input("\nThat ingredient is not on the list.\n\nWould you like to try for another ingredient?\nyes or no?\n\n")
            if try_again == "yes":
                ingredient_to_authenticate = input("\n\nWhat other ingredient would you like to check for in the list? ")
            elif try_again != "yes":
                print("\nGoodbye")
                ingredient_in_list = True

ingredients_list = ["Tomato", "Salt", "Pepper", "Vinegar", "Sugar"]           
print(ingredient_finder(ingredients_list))



# Task 9, define a funtion that takes in a list and returns the list with flipped values
    # Steps to solve this challenge:
        # 1}    define a funtion that takes in a list parameter
        # 2}    flip the list using [start, stop, step]
        # 4}    return the list
def list_flipper(list):
    new_list = list[::-1]
    return new_list
   

spongebob_friends = ["tissue", "chip", "penny"]
print(list_flipper(spongebob_friends))



# Task 10, create a function that returns list that only containes names with 4 letters in it
    # Steps to solve this challange:
        # 1}    define a function that takes in a list
        # 2}    extract every name from the list individually
        # 3}    create a loop that runs while there are still elements in the list
        # 3}    if the string has 4 characters, add it to the new list
        # 4}    return the new list
def four_or_more_letters(list):
    new_list = []
    index = 0
    while index != len(list):
        name = list[index]
        if len(name) > 4:
            new_list.append(name)
            index += 1
        else:
            index += 1
    return new_list

list_of_names = ["Josh", "Jackson", "Jay", "Jr", "Jacky", "Jasper"]
print(four_or_more_letters(list_of_names))