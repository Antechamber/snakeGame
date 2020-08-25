from random import randint

moves = ["Rock", "Paper", "Scissors"]

player = False
while not player:
    player = input("Rock, Paper or Scissors? ")
    computer = randint(0, 2)
    if moves.__contains__(player):
        if (moves.index(player) + 2) % 3 == computer:
            print("Player wins!: " + player + " beats " + moves[computer] + " :D")
            player = False
        elif player == moves[computer]:
            print("Tie: " + player + " and " + moves[computer])
            player = False
        elif (moves.index(player) + 1) % 3 == computer:
            print("Player loses: " + moves[computer] + " beats " + player + " ;(")
            player = False
        else: print("ERROR")
        player = False
    else:
        print("Please choose a valid move...")
        player = False

