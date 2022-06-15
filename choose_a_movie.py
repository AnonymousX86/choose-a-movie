# -*- coding: utf-8 -*-
from random import choice


def main():
    try:
        with open('movies.txt') as f:
            movies = f.readlines()
    except FileNotFoundError:
        print('File not found, creating "movies.txt". Now add some movies'
              ' inside, and run the program again.')
        with open('movies.txt', 'x'):
            pass
        return
    if not movies:
        print('No movies found, please add some movies inside "movies.txt"')
        return
    print(f'The prophecy says: {choice(movies)}')


if __name__ == '__main__':
    main()
