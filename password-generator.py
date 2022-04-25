import random

#these characters will be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
combined_list = [letters, numbers, symbols]

#prompting the user to receive information about the desired password
print("Welcome! This program generates a random password. You're the one to choose how many letters, numbers and symbols you want.")
number_of_letters= int(input("How many letters would you like in your password?\n")) 
number_of_numbers = int(input("How many numbers would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like in your password?\n"))

#putting number of desired characters in a list so that their index would match the respective index in the combined list.
#this way we will be able to check the number of desired characters easily
desired_characters = [number_of_letters, number_of_numbers, number_of_symbols]
password = ""
length_of_password = sum(desired_characters)
#adding random characters limited by the number of desired characters to the password until the length of password reaches
#the sum of the number of desired characters
while len(password) != length_of_password:
    random_combinedlist_index = random.randint(0, len(combined_list) - 1)
    random_list_index = random.randint(0, len(combined_list[random_combinedlist_index]) - 1)
    if desired_characters[random_combinedlist_index] > 0:
        password += str(combined_list[random_combinedlist_index][random_list_index])
        desired_characters[random_combinedlist_index] -= 1
print(password)        


