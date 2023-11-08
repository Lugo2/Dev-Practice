
import random
city_list=['Tijuana','Lima','Amsterdam','Cairo','Bangkok','Melbourne']
eats_list = ['Tacos el Gordo', 'Bodega de Trattoria','Vapiano', 'Hamada Sheraton', 'Sen', 'Chin Chin']
transportation_list = ['taxi', 'metro', 'bicycle rental', 'on foot', 'Skytrain', 'tram']
entertainment_list=['Mamut cerveceria', 'Lacro Museum', 'Canal Cruise', 'Cairo Citadel', 'Siam Park', 'Flemington Racecourse']


print("\nWelcome!\n\nLooking for a completely random travel experience?\nYou've come to the right place!\n\nNow, lets get to mixin'!")

def rand_location(location_list):
    location = random.choice(location_list)
    return location

def rand_restaurant(grub_list):
    grub = random.choice(grub_list)
    return grub

def rand_transportation(vehicle_list):
    vehicle = random.choice(vehicle_list)
    return vehicle

def rand_entertainment(entertain_list):
    entertainment = random.choice(entertain_list)
    return entertainment