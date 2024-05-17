
import random

print("Welcome to random password generator")
random_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz€!@#$%^&*<>1234567890"
number_of_passwords = int(input("Please enter the number of passwords to generate: "))
password_length = int(input("Please enter the length of the password needed: "))

print("Here are your random passwords:")
for _ in range(number_of_passwords):
    password = ""
    for _ in range(password_length):
        password += random.choice(random_chars)
    print(password)

