print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
wins_counter = 0
game_on = True

while game_on:
    decision = input("You are at the top of a mountain, you have two roads. Where do you want to go? Type left or right: ")

    if decision == 'left':
        decision2 = input("You come to a lake and see an island in the middle of it. What are you doing? Type wait or swim: ")
        if decision2 == 'swim':
            decision3 = input("You swim to the island and notice there is a house with 3 doors. Which door are you opening? Type blue, red or yellow: ")
            if decision3 == 'yellow':
                print("You Won! Congratulations!")
                wins_counter += 1
                break
            elif decision3 == 'red':
                print("You have been burned by fire! You died.")
                print("Game over!")
                break
            elif decision3 == 'blue':
                print("You have been eaten by beasts! You died.")
                print("Game over!")
                break
            else:
                print("Game over!")
                break

        else:
            print("You have been attacked by a trout! You died.")
            print("Nice try, game over!")
            break
    else:
        print("You have encountered a bear! You died.")
        print("Game Over!")
        break

    play_again = input("Do you want to play again? Type y or n: ")
    if play_again == 'n':
        print("Thanks for playing!")
        break
    else:
        play_again = True