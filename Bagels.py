import sys
import random

correct_answer = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]


def answer_to_list(player_answer):
    try:
        player_answer = list(map(int, player_answer.strip()))
    except ValueError:
        return print('Must be a number')
    return player_answer


def check_answer(player_answer, correct):
    answer_list = player_answer[:]
    output = ''
    if answer_list == correct:
        return print('You WON!'), sys.exit()
    for i in range(3):
        if answer_list[i] == correct[i]:
            output += 'Fermi '
            answer_list[i] = None
    for digit in answer_list:
        if digit in correct:
            output += 'Pico '
    if output == '':
        return print('Bagel')
    return print(output)


def game():
    tries = 10
    while tries > 0:
        player_answer = input('Provide me a 3 digit number: ')
        if player_answer == 'QUIT':
            print('See you soon!'), sys.exit()
        if len(player_answer) != 3:
            print('Must be 3 digits only.')
        else:
            player_answer = answer_to_list(player_answer)
            check_answer(player_answer, correct_answer)
            tries -= 1
            print(f'Your guess was {player_answer}. Tries left: {tries}')
    else:
        print(f'You LOSE! Correct answer was {correct_answer}')


if __name__ == "__main__":
    game()
