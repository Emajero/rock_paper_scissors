import random

# from test import is_win
alist = ['r', 'p', 's']
print(alist)

def play():
    user = input("Select an option above: \n")
    user = user.lower

    computer = random.choice(alist)
    print(computer)

    if user == computer:
        return "Player: {}\n Computer: {}. It's a tie!" .format(user, computer)

    if is_win(user, computer):
        return "Player {}\n Computer:{}. You won!" .format(user, computer)

    return "Player{}\n Computer:{}. You lost!" .format(user, computer)


def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    return False

if __name__ == '__main__':
    print(play())





