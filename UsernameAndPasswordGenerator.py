#Importing the random and string libraries
import random 
import string
import csv

#Functions for usernames and passwords
def generate_username(first, last):
    variations = [
        first[0].lower() + last.lower(),
        first.lower() + "." + last[0].lower(),
        last.lower() + str(random.randint(10, 99)),
        first.lower() + last.lower()
    ]
    return random.choice(variations)

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

#Combining and displaying usernames and passwords
first = input("Enter first name")
last = input("Enter last name")
length = int(input("Enter password length:"))

username = generate_username(first, last)
password = generate_password(length)

print(f"\nGenerated username: {username}")
print(f"Generated password: {password}")

#Saving the results 
with open("credentials.txt", "a") as file:
    file.write(f"Username: {username}, Password: {password}\n")
#This is for an excel file
#import csv
#with open("credentials.csv", "a", newline="") as file:
    #writer = csv.writer(file)
    #writer.writerow([username, password])

#Option for what is printed
print("Choose an option:")
print("1 - Generate Username only")
print("2 - Generate Password only")
print("3 - Generate Both")

choice = input("Enter choice: ")

if choice == "1":
    username = generate_username(first, last)
    print(f"Generated username: {username}")
    with open("credentials.txt", "a") as file: 
        file.write(f"Username: {username}\n")

elif choice == "2":
    password = generate_password(length)
    print(f"Generated password: {password}")
    with open("crentials.txt", "a") as file:
        file.write(f"Password: {password}\n")

elif choice == "3":
    username = generate_password(first, last)
    password + generate_password(length)
    print(f"Generated username: {username}")
    print(f"Generated password: {password}")
    with open("credentials.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")

else:
    print("\nInvalid choice. Please select 1, 2, or 3.")
    