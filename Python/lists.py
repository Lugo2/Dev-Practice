# Task 1, create a function that accesses a list element
    # Steps to overcome the challange:
        # 1}    create a list of tech stacks
        # 2}    define a function that returns the second item in the list
        # 3}    print result to console
tech_stacks = ["Java", "Python", "JavaScript", "Django", "React"]

def second_element(list):
    second_value = list[1]
    return second_value

print(f"\n{second_element(tech_stacks)}\n")



# Task 2, create a function that adds and changes elements from a list
    # Steps to overcome the challange:
        # 1}    create a list of names
        # 2}    define a function that takes in a list as an argumant and adds 2 elements to the list
        # 3}    check for duplicates in the list
        # 4}    append the number of duplicte to the back of the duplicate element
def add_name_to_list(new_elements, current_list):
    
    for name in new_elements:

        if name in current_list:
            duplicate_count = 2
            name += str(duplicate_count)
            current_list.append(name)
        else:
            current_list.append(name)
    new_list = current_list
    return new_list

names = ["Dan", "Ben", "John", "Rod", "Sam", "Bob", "Joe"]
print(f"\nThis is the current list of names: {names}.")
user_input = input("\nWhat names would you like to add to the list? ")
user_input_list = user_input.split(", ")
new_names_list = add_name_to_list(user_input_list, names)

print(f"\nThis is the new list of names: {new_names_list}\n")



# Task 3, create a function that subtracts a name and returns a new names list using pop()
    # Steps to overcome the challange:
        # 1}    use the list from the previous task
        # 2}    define a function that returns a new list with a name subracted
        # 3}    use list.pop() to get rid of a name
        # 4}    return the list with the name subtracted
def subtract_using_pop(list):
    print(f"\nThe current list of names is{new_names_list}\n")
    name_to_subtract = input("What name would you like to get rid of in the list? ")
    list.pop(list.index(name_to_subtract))
    return list

new_names_list_2 = subtract_using_pop(new_names_list)

print(f"\nThis is the new list of names with a name subtracted using pop(): {new_names_list_2}\n")



# Task 4, combine each value of the same index from 2 lists and return a list with the combined values
    # Steps to overcome the challange:
        # 1}    create 2 lists
        # 2}    define a function that takes in 2 lists and uses a loop to concate elements from each list
        # 3}    create a for loop that loops through the contents of the first list
        # 4}    within the for loop use index(element) on the first list to get the index number to extract the corrisponding element from the list
        # 5}    concatenate bothj elements and put into a list
        # 6}    once all elements in list one have eterated, return the new list with concatenated values from both lists
list_1 = ["fan", "bull-", "high-", "barrel-o-", "slap"] 
list_2 = ["dango", "rider", "horse", "monkeys", "stick"]

def string_concatenator(list1, list2):
    concatenated_strings = []
    for list_1_element in list1:
        index_list_1 = list1.index(list_1_element)
        list_2_element = list2[index_list_1]
        concatenated_strings.append(list_1_element + list_2_element)
    return concatenated_strings

print(f"\n{string_concatenator(list_1, list_2)}\n")



# Task 5, create a function that adds a name to a list only if its not a duplicate and asks for a nickname if it is a duplicate
    # Steps to overcome the challange:
        # 1}    declare a list with names, a variable with a name value, and a variable containing a boolean to check if the dup has been found
        # 2}    define a for loop that takes a list and a variable compares the name variable to a element name of the list
        # 3}    create conditional statements to determine printing a message that a duplicate was found or printing the list with the added elements if not
        # 4}    return the list
friends = ["Jalvich", "Jen", "Lupe", "Ludwig", "Oscar", "Okonkwo"]
friend_to_add_string = input(f"\nName a friend your like to add to the list: ")

def add_to_friends_list(list, friend):
    duplicate = True
    while duplicate == True:
        if friend in list:
            friend = input(f"\nSorry, that name is taken, please enter a nickname: ")
            if friend in list:
                friend = input(f"\nSorry, that name is taken too, please enter a nickname: ")
        else:
            list.append(friend)
            duplicate = False
    return list

print(f"\n{add_to_friends_list(friends, friend_to_add_string)}\n")



# Task 6, show all 3 ways to copy a list, not make a referance to it
favorite_vehicles = ["79' BMW 2002 Turbo", "83' Lancia 037 Stradale", "72' c10"]
    # Steps for using .append():
        # 1}    use a for loop to get each element from the list
        # 2}    use .append(element) to add to the new list
        # 3}    once the loop is over, return the new list with the same elements as the first list
appended_list = []
for element in favorite_vehicles:
    appended_list.append(element)


    #  Steps for using copy():
        # 1}    use .copy(list) to copy every element from the first list on to a new list 
        # 2}    return the new list
copied_list = favorite_vehicles.copy()


    #  Steps for using list():
        # 1}    use list(list) to create a new variable with list elements from the first list
        # 2}    return the new list
listed_list = list(favorite_vehicles)


print(appended_list)
print(copied_list)
print(listed_list)


# Task 7, sort the items in a list alphabetically ascending, descending, and alphanumerically ordered from most letters to least

favorite_dishes = ["Enchiladas", "Hotdogs", "Tortas", "Ceviche", "Aguachile"]

    # Sort ascending:
favorite_dishes.sort()
print(favorite_dishes)

    # Sort descending:
favorite_dishes.sort(reverse = True)
print(favorite_dishes)

    # Sort alphanumerically from most to least:
def alphanumeric(list):
    return len(list)

favorite_dishes.sort(reverse = True, key = alphanumeric)
print(favorite_dishes)