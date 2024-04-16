import random
user_action = input('Enter any one(stone, paper, scissors):')
choices = ['stone', 'paper', 'scissors']
computer_action = random.choice(choices)
print(f'You choose {user_action} vs computer choose {computer_action}.\n')

if user_action == computer_action:
    print(f'Both players selected {user_action} & its a tie')
elif(user_action == 'stone'):
    if(computer_action == 'scissors'):
        print(f'{user_action} beats {computer_action}, You Win!')
    else:
        print(f'{computer_action} beats {user_action}, You Lose!')
elif(user_action == 'paper'):
    if(computer_action == 'stone'):
        print(f'{user_action} beats {computer_action}, You Win!')
    else:
        print(f'{computer_action} beats {user_action}, You Lose!')
elif(user_action == 'scissors'):
    if(computer_action == 'paper'):
        print(f'{user_action} beats {computer_action}, You Win!')
    else:
        print(f'{computer_action} beats {user_action}, You Lose!')