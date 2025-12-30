# a = 0
# Correctly assigning inputs to variables
# name = input("Tell Bilal full name: ")
# age = int(input("Tell Bilal age: "))
# city = input("Tell Bilal city: ")
# love = input("Tell Bilal love: ")

# # Checking conditions
# if name == "Muhammad Bilal":
#     a += 1
# if age == 22:
#     a += 1
# if city == "faisalabad":
#     a += 1
# if love == "Allah":
#     a += 1

# Displaying the score
# print("Your score is:", a, "out of 4")

#: Excercise:3

# Create a program capable of displaying Questions to the user like KBC
# Use list data-type to store the questions and their correct answers
# Display the final amount the person takes home post game-play

# Get the player's name
name = input("What is your name?\n")
print(f"\nGood to have you, {name}! Welcome to Kaun Banega Crorepati!\n")
print("Here is your first question:\n")

# List of questions and answers
questions = [
    "What is the capital of India? ",
    "Who won the FIFA World Cup 2022? ",
    "How many planets are there in the Solar System? ",
    "What is the value of g (acceleration due to gravity in m/s^2)? "
]

answers = ["delhi", "argentina", "8", "9.8"]
prizes = [1000, 2000, 3000, 4000]  # Prize money for each correct answer

# Initialize the prize money
total_winnings = 0

# Loop through questions
for i in range(len(questions)):
    user_answer = input(questions[i]).lower()  # Convert answer to lowercase
    if user_answer == answers[i]:
        total_winnings += prizes[i]
        print(f"Correct answer! You have won {total_winnings} INR\n")
    else:
        print(f"Wrong answer. Your take-home amount is {total_winnings} INR\n")
        break  # End the game if the answer is wrong

# Ending message
print(f"It was great playing with you, {name}! You won a total of {total_winnings} INR.")