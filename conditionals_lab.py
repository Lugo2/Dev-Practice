import random

# Task 1
legal_driving_age = 16
prompt_user = input("What's your age? ")
user_age = int(prompt_user)

if user_age >= legal_driving_age:
    print("You are legally able to drive.")

elif user_age < legal_driving_age:
    print("You are not legally of age to drive.")



# Task 2
random_number = random.randint(0, 11)

if random_number <= 2:
    print("0 or 1 or 2")

elif random_number >= 3 and random_number <=5:
    print("3 or 4 or 5")

elif random_number >= 6 and random_number <= 8:
    print("6 or 7 or 8")
    
elif random_number >= 9 and random_number <= 11:
    print("9 or 10 or 11")



# Task 3
user_fav_team = input("What's your favorite football team? ")

if user_fav_team == "Bears":
    print("Quarterback much?")

elif user_fav_team == "Vikings":
    print("Loud noises!")

elif user_fav_team == "Lions":
    print("LOL! They trash!")

elif user_fav_team == "Packers":
    print("Best team in the world! Actually, the universe!")

else:
    print("Pick a different team. ")