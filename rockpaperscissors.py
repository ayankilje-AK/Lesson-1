import random

while True:
    player_1 = input("Enter a choice. Rock, Paper or Scissors: ")
    possible_actions = ["Rock", "Paper", "Scissors"]
    player_2 = random.choice(possible_actions)
   
    print(f"\nYou chose {player_1}, and the opponent chose {player_2}.")

    if player_1 == player_2:
        print(f"Both players selected {player_1}. It is a draw.")
    elif player_1 == ("Rock"):
        if player_2 == ("Scissor"):
            print("Rock smashes scissor. Player 1 wins")
        else:
            print("Paper covers Rock. Player 2 Looses.")
    elif player_1 == ("Paper"):
        if player_2 == ("Rock"):
            print("Paper covers Rock. Player 1 wins!")
        else:
            print("Scissor cuts paper. Player 2 Wins!")
    elif player_1 == ("Scissors"):
        if player_2 == ("Paper"):
            print("Scissor cuts through paper. Player 1 Wins!")
        else:
            print("Rock smashes scissor. Player 2 Wins!")
    play_again = input("Do you want to Play Again? Yes or No")
    if play_again != ("Yes"):
        break
    
        
