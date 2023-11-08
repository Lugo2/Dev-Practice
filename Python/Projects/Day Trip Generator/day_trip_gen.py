
import random
city_list=['Tijuana','Lima','Amsterdam','Cairo','Bangkok','Melbourne']
eats_list = ['Tacos el Gordo', 'Bodega de Trattoria','Vapiano', 'Hamada Sheraton', 'Sen', 'Chin Chin']
transportation_list = ['taxi', 'metro', 'bicycle rental', 'on foot', 'Skytrain', 'tram']
entertainment_list=['Mamut cerveceria', 'Lacro Museum', 'Canal Cruise', 'Cairo Citadel', 'Siam Park', 'Flemington Racecourse']


print("\nWelcome!\n\nLooking for a completely random travel experience?\nYou've come to the right place!\nNow, lets get to mixing!\n")

def rand_element(e):
    element = random.choice(e)
    return element

def trip_generator():
    location = rand_element(city_list)
    grub = rand_element(eats_list)
    vehicle = rand_element(transportation_list)
    entertainment = rand_element(entertainment_list)
    return f"Destination: {location}\nFood: {grub}\nMode of Transportation: {vehicle}\nForm of Entertainment: {entertainment}\n"

user_input = input(f"\nHere's your completely randomized trip itinerary.\n\n{trip_generator()}\n\nAre you satisfied with your current trip?\nType yes or no\n\n")

user_satisfied = False
while user_satisfied != True:
    if user_input == "yes":
        print("\nGreat, hope you have tons of fun!")
        user_satisfied = True
    elif user_input != "yes":
        user_change = input("\nSorry to hear that, what part would you like to change?\nLocation? Food? Vehicle? Entertainment? ")
        if user_change == "Location":
            