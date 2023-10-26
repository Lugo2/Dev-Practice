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