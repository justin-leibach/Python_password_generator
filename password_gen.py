# Created from Dr Angela Yu's python 100 day bootcamp. Provided was line 3-13
# Line 15-37 is my original work

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Create empty lists
random_letters = []
random_symbols = []
random_numbers = []

#iterate through input 
for i in range(0, nr_letters):
  #append a randomized choice of letters to empty list created above
  random_letters.append(random.choice(letters))

for i in range(0, nr_symbols):
  random_symbols.append(random.choice(symbols))

for i in range(0, nr_symbols):
  #randomize
  random_symbols.append(random.choice(symbols))

#create one list from all the randomized lists
final_pass = random_letters + random_numbers + random_symbols

#print a final list using join function to convert list to string
print("Your final randomized password is:")
print(''.join(final_pass))

