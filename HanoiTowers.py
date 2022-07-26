import re

TOWERS = {
    'A': [5, 4, 3, 2, 1],
    'B': [],
    'C': [],
}


def draw_towers():
    empty_segment = '     ||     '
    print(empty_segment * 3)
    for i in range(4, -1, -1):
        row = ''
        for tower, disks in TOWERS.items():
            if i < len(disks):
                disk_half = ' '*(5-disks[i]) + '@'*disks[i]
                row += disk_half + '_' + str(disks[i]) + disk_half[::-1]
            else:
                row += empty_segment
        print(row)
    print(' '*6 + 'A' + ' '*11 + 'B' + ' '*11 + 'C')


def move(user_move):
    # Check user input
    pattern = '[ABC][ABC]'
    if len(user_move) != 2 or not re.match(pattern, user_move):
        return print('Incorrect input')

    first_tower, second_tower = user_move

    if not TOWERS[first_tower]:
        return print(f'Tower {first_tower} is empty')
    if TOWERS[second_tower] and TOWERS[second_tower][-1] < TOWERS[first_tower][-1]:
        return print('Larger discs cannot rest on top of a smaller disk')

    moving_thing = TOWERS[first_tower].pop()
    TOWERS[second_tower].append(moving_thing)
    return draw_towers()


def run_game():
    print('Welcome to the Hanoi Towers')
    draw_towers()

    while TOWERS['B'] or TOWERS['C'] != [5, 4, 3, 2, 1]:
        next_move = input('Enter your move: ')
        if next_move == 'exit':
            return print('See you soon!')
        move(next_move)
    return print(f'Congratulations! You won!')


if __name__ == "__main__":
    run_game()
