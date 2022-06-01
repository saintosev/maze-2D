import sys
import os

WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

PLAYER = '@'
BLOCK = chr(9617)


def displayMaze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (playerx, playery):
                print(PLAYER, end='')
            elif (x, y) == (exitx, exity):
                print('X', end='')
            elif maze[(x, y)] == WALL:
                print(BLOCK, end='')
            else:
                print(maze[(x, y)], end='')
        print()


print('Maze-файлы сгенерированы mazemakerrec.py')

while True:
    print('Введи название файла или LIST для отображения всех файлов или QUIT для выхода из программы):')
    filename = input('> ')

    if filename.upper() == 'LIST':
        print('Maze-файлы найдены в', os.getcwd())
        for fileInCurrentFolder in os.listdir():
            if (fileInCurrentFolder.startswith('maze') and
                    fileInCurrentFolder.endswith('.txt')):
                print('  ', fileInCurrentFolder)
        continue

    if filename.upper() == 'QUIT':
        sys.exit()

    if os.path.exists(filename):
        break
    print('Не существует файла с названием', filename)

mazeFile = open(filename)
maze = {}
lines = mazeFile.readlines()
playerx = None
playery = None
exitx = None
exity = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (
            WALL, EMPTY, START, EXIT), 'Недопустимый сивмол в столбце {}, строке {}'.format(x + 1, y + 1)
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            playerx, playery = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert playerx != None and playery != None, 'В maze-файле нет начала.'
assert exitx != None and exity != None, 'В maze-файле нет выхода.'

while True:
    displayMaze(maze)

    while True:
        print('                             W')
        print('Задай направление или QUIT: ASD')
        move = input('> ').upper()

        if move == 'QUIT':
            print('Спасибо за игру!')
            sys.exit()

        if move not in ['W', 'A', 'S', 'D']:
            print('Недопустимое направление. Введи W, A, S или D')
            continue

        if move == 'W' and maze[(playerx, playery - 1)] == EMPTY:
            break
        elif move == 'S' and maze[(playerx, playery + 1)] == EMPTY:
            break
        elif move == 'A' and maze[(playerx - 1, playery)] == EMPTY:
            break
        elif move == 'D' and maze[(playerx + 1, playery)] == EMPTY:
            break

        print('Ты не можешь двигаться в этом направлении.')

    if move == 'W':
        while True:
            playery -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery - 1)] == WALL:
                break
            if (maze[(playerx - 1, playery)] == EMPTY
                    or maze[(playerx + 1, playery)] == EMPTY):
                break
    elif move == 'S':
        while True:
            playery += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery + 1)] == WALL:
                break
            if (maze[(playerx - 1, playery)] == EMPTY
                    or maze[(playerx + 1, playery)] == EMPTY):
                break
    elif move == 'A':
        while True:
            playery -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx - 1, playery)] == WALL:
                break
            if (maze[(playerx, playery - 1)] == EMPTY
                    or maze[(playerx, playery + 1)] == EMPTY):
                break
    elif move == 'D':
        while True:
            playery += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx + 1, playery)] == WALL:
                break
            if (maze[(playerx, playery - 1)] == EMPTY
                    or maze[(playerx, playery + 1)] == EMPTY):
                break

    if (playerx, playery) == (exitx, exity):
        displayMaze(maze)
        print('Ты нашёл выход! Поздравляю!')
        print('Спасибо за игру!')
        sys.exit()
