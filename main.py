
#1
number = 1
while number <= 1000:
    if number % 3 == 0:
       print(f"{number} is divisible by 3.")
    number += 1

#2
value = float(input("Give a value to convert from inches to centimeters: "))
def value_in_centimeters (value):
    return value * 2.54
roll_no = 0
while value >= 0:
    if value > 0:
        print(f"Value in centimeters: {value_in_centimeters (value)}")
    elif value == 0:
        print(f"Value in centimeters is O.")
    value = float(input(f"Give a value to convert from inches to centimeters: "))
    roll_no += 1
print("Sorry, unable to execute.")

#3

user_input = input("Enter a number (or press Enter to quit): ")
if user_input == "":
    print("Thank you for playing. See you next time!")
else:
    smallest = float(user_input)
    largest = float(user_input)
    while user_input != "":
        user_input = input("Enter a number (or press Enter to quit): ")
        if user_input == "":
            break
        num = float(user_input)
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
    print("Thank you for playing. See you next time!")

#4
import random
secret_number = random.randint(1, 10)
attempts = 0
user_guess = 0
while user_guess != secret_number:
    user_guess = int(input("Guess the number between 1 and 10: "))
    attempts += 1
    if user_guess == secret_number:
        print(f"Correct! You guessed the number {secret_number} in {attempts} attempts.")
    elif user_guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

#5
correct_username = "python"
correct_password = "rules"
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        print("Incorrect username or password. Please try again.")
        attempts += 1
if attempts == max_attempts:
    print("Access denied. You have reached the maximum number of login attempts.")

#6
import random
num_points = int(input("Enter the number of random points to generate: "))
points_inside_circle = 0
total_points = 0
while total_points < num_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        points_inside_circle += 1
    total_points += 1
approx_pi = 4 * points_inside_circle / total_points
print(f"Approximation of pi: {approx_pi}")
