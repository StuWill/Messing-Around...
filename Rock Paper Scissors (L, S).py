from random import randint

def switchy(arg, user): #equivalent of switch statement (cases)
  choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
    4: "Lizard",
    5: "Spock"
  }
  choice = choices.get(arg, "invalid choice")
  if user == 0:
    print('You:', choice, '....vs....', end=' ')
  else:
    print('Computer:', choice)

turn = 1
while turn < 4:
  player = int(input('Rock (1), Paper (2), Scissors (3), Lizard (4) or Spock (5)?'))

  switchy(player, 0)

  comp = randint(1,5)
  #print(comp)
  switchy(comp, 1)

  if player == 1 and comp == 3:
    print("Rock crushes Scissors. You win!")
    break
  elif player == 3 and comp == 2:
    print("Scissors cuts Paper. You win!")
    break
  elif player == 2 and comp == 1:
    print("Paper covers Rock. You win!")
    break

  #added lizard spock if else statements.

  elif player == 1 and comp == 4:
    print("Rock crushes Lizard. You win!")
    break
  elif player == 3 and comp == 4:
    print("Scissors decapitates Lizard. You win!")
    break
  elif player == 2 and comp == 5:
    print("Paper disproves Spock. You win!")
    break
  elif player == 4 and comp == 5:
    print("Lizard poisons Spock. You win!")
    break
  elif player == 4 and comp == 2:
    print("Lizard eats Paper. You win!")
    break
  elif player == 5 and comp == 3:
    print("Spock smashes Scissors. You win!")
    break
  elif player == 5 and comp == 1:
    print("Spock vaporises Rock. You win!")
    break
    #gives you another turn if there's a tie or loss
  else:
    if player == comp:
      print("Looks like we have a tie!")
      turn += 1
    else:
      print("Computer wins. You lose!!")
      turn += 1
