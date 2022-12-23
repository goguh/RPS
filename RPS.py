import random

def get_choices():
  player_choices = input('Enter your choice (rock, paper, scissors):')
  options = ['rock', 'paper', 'scissors']
  computer_choices = random.choice(options)
  choices = {'player': player_choices , 'computer': computer_choices}
  return choices
     
def check_win(player, computer):
  print(f'You chose {player}, computer chose {computer}')
  if player == computer:
    return 'Its a tie'
  elif player == 'rock':
    if computer == 'scissors':
      return 'rock smashes scissors, you win'
    else:
      return 'paper cover rock, you lose'
    elif player == 'paper':
      if computer == 'rock':
        return 'paper covers rock, you win'
      else:
        return 'scissors cut paper, you lose'
      elif player == 'scissors':
        if computer == 'paper':
          return 'scissors cut paper, you win'
        else:
          return 'rock smashes scissors, you lose'
 
choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)
