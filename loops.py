
# For Loops
    # Task 1, for everytime x iterates print "Hello"
for x in range(5): 
    print("Hello")



    # Task 2, uses x to print 0-10 as specified by range argument
for x in range(11): 
    print(x)



    # Task 3, uses range(start, stop, step) to count backwards
for x in range(10, -1, -1): 
    print(x)



    # Task 4, prompts user for how many times "Boardem'" should print
user_input = input("How many times would you like the loop to run? ")
number_of_iterations = int(user_input)

for x in range(number_of_iterations):
    print("Boardem'")



    # Task 5, prints every letter in "Packers"
p = "Packers"
for letter in p:
    print(letter)



    # Task 6, prints every number 0-100 except if divisable by 3 or 5 or both
for number in range(100):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)



# While Loops
    # Task 1, prints "hello" to terminal as many times as user specifies 

user_eterations = int(input("How many times should I say hello? "))
eteration = 0
condition = True
while condition is True:
    if eteration < user_eterations:
        print("Hello")
        eteration += 1
    else:
        condition = False



    # Task 2, prompts user for a password, reprompts to check for validation
user_set_password = input("New password: ")
incorrect_password = True
logged_in = print("\nUser Validated\n\nYour're in! Cool! Now get out.\n*Poof*")

while incorrect_password == True:
    login_attempt = input("\nPassword: ")
    if user_set_password == login_attempt:
        print("\nUser Validated")
        incorrect_password = False
    else:
        print("\nTry Again Goofy!")