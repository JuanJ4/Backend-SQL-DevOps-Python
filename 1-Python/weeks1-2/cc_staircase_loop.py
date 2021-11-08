import random
stars = ""
for i in range(0, 5, 1):
    for j in range(0, i, 1):
        stars += "*"
        print(stars)


# def reverse(str):
#     return str[::-1]

# name = input("What is your name? ")
# print("Your name reversed is:", reverse(name))


# high_score = 0


# def dice_game():


# while True:
# global high_score
# print("Current High Score: ", high_score)
# print("1) Roll Dice")
# print("2) Leave Game")
# choice = input("Enter Your Choice: ")

# if choice == "1":
# die1 = random.randint(1, 6)
# die2 = random.randint(1, 6)
# totaldie = die1 + die2
# print("You roll a...", die1)
# print("You roll a...", die2, "\n")
# print("You have rolled a total of: ", totaldie, "\n")
# if totaldie > high_score:
# high_score = totaldie
# print("New High Score!", high_score, "\n")

# elif choice == "2":
# print("Goodbye!")
# break


# dice_game()


# import random

# high_score = 0

# def dice_game():
#     while True:
#         global high_score
#         print("Current High Score:", high_score)
#         print("1) Roll Dice")
#         print("2) Leave Game")
#         choice = input("Enter your choice: \n")
#         if choice == "1":
#             dice1 = random.randint(1,6)
#             dice2 = random.randint(1,6)
#             total = dice1 + dice2
#             print("You roll a...", dice1)
#             print("You roll a...", dice2, "\n")
#             print("You have rolled a total of:", total, "\n")
#             if total > high_score:
#                 high_score = total
#                 print("New high score!\n")
#         elif choice == "2":
#             break


# dice_game()
