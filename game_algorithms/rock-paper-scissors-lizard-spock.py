import random


def modify_rock_paper_scissors(your_pick):
    elements = {
        'rock': ['spock', 'paper'],
        'paper': ['scissors', 'lizard'],
        'scissors': ['rock', 'spock'],
        'lizard': ['scissors', 'rock'],
        'spock': ['lizard', 'paper']
    }
    bot_pick = random.choice(list(elements.keys()))
    if your_pick not in elements:
        return 'Not Valid Pick!'
    if your_pick == bot_pick:
        return 'Equal!'
    if bot_pick in elements[your_pick]:
        return f'You lose with {your_pick}, Bot win with {bot_pick}!'
    return f'You win with {your_pick}, Bot lose with {bot_pick}!'


print(modify_rock_paper_scissors('rock'))