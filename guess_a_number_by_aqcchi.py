# GuessANumberByaqcchi
import random
number_of_tries = 0
computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number(1, 100): ")
    number_of_tries += 1

    if not player_input.isdigit():
        print("Invalid input! Try again...")
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        print("You guessed it!")
        break
    elif player_number > computer_number:
        if number_of_tries > 4:
            print("No more tries left! GAME OVER!")
            break
        print("Too High! Try again!")
    else:
        if number_of_tries > 4:
            print("No more tries left! GAME OVER!")
            break
        print("Too Low! Try again!")



