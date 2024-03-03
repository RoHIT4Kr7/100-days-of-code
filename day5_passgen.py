import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
storeletter=""
for letter in range(0,(nr_letters)):
    storeletter+=random.choice(letters)
storesymbols=""
nr_symbols = int(input(f"How many symbols would you like?\n"))
for symbol in range(0,(nr_symbols)):
    storesymbols+=random.choice(symbols)
nr_numbers = int(input(f"How many numbers would you like?\n"))
storenumbers=""
for number in range(0,(nr_numbers)):
    storenumbers+=random.choice(numbers)

Finalpassword=(storenumbers+storeletter+storesymbols)
pass_len=len(Finalpassword)
# print(Finalpassword)
randompass=[]
newlist=[]
for n in Finalpassword:
    newlist.append(n)
randompass += random.sample(newlist,pass_len)
Output_password=''.join(randompass)
print(f"Your Password is: {Output_password}")