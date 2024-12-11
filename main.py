#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""

# # for each of the selected number of letters, symbols and numbers, retrieve a random value in the letters list and append it to password string
# for char in range(1, nr_letters + 1):

	# original method - assigns new random character and adds to the password
	# random_char = random.choice(letters)
	# password = password + random_char

	# This does same as above, but shorter/cleaner method
# 	password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
# 	password += random.choice(symbols)
	
# for char in range(1, nr_numbers + 1):
# 	password += random.choice(numbers)

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# This time, instead of printing out a password string, add as a list instead.  Then we can randomize the order of that list
password_list = []

# for each of the selected number of letters, symbols and numbers, retrieve a random value in the letters list and append it to password string
for char in range(1, nr_letters + 1):
	password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
	password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
	password_list.append(random.choice(numbers))

# print(password_list)  # Displays the original order
random.shuffle(password_list)  # Shuffles the list above
# print(password_list)  # Displays the new shuffled order

# Convert list back to a string
password = ""

for char in password_list:
	password += char

print(f"Your password is: {password}")
