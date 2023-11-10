import random
favorite_number = 9

# Task 1, generate a random number between a range that includes your favorite number and check how many numbers away the randome number is to your favorite number
    # To complete task:
        # 1}    create a variable and set it equal to a random module to generate a number between a range that includes your favorite number
        # 2}    use conditional statments to compare the random number to your favorite number
        # 3}    if your favorite number < the random number, use a for loop in a range between your fav number and the random number to get the amount between
        # 4}    if your favorite number > the random number, use a for loop in a range between your fav number and the random number to get the amount between
        # 5}    print to console

rand_num = random.randint(0, 19)

if favorite_number < rand_num:
    num_between = 0
    favorite_number += 1
    for num in range(favorite_number, rand_num):
        num_between += 1
    favorite_number -= 1
    print(f"\nThis is how many numbers are between {favorite_number} and {rand_num}: {num_between}\n")
elif favorite_number > rand_num:
    num_between = 0
    rand_num += 1
    for num in range(rand_num, favorite_number):
        num_between += 1
    rand_num -= 1
    print(f"\nThis is how many numbers are between {rand_num} and {favorite_number}: {num_between}\n")



# Task 2, create a loop that generates a random number and checks if it matches your fav number
    # To complete task:
        # 1}    create a variable with a bool value and while loop since who knows how many times the program will have to guess
        # 2}    create a variable called "count" to store the amount of times it guesses wrong
        # 3}    print the amount of times it took to guess right

correct_guess = False
count = 0

while correct_guess == False:
    random_number = random.randint(0, 10)
    if favorite_number == random_number:
        count += 1
        print(f"\nI had to guess your favorite number this many times: {count}\n")
        correct_guess = True
    if favorite_number != random_number:
        count += 1