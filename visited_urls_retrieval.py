"""This script turns the visited URLs written to the downloads log into a `visited.json`
which can be put into a project of the `./urls` directory such that these images will not
be duplicated."""

# Python libs
from re import findall
from os import path
import json

#
from tqdm import tqdm

URL_PATTERN = r'http.*[0-9]'

def main():
    print('Searching for URLs...')

    founds = []
    with open(path.abspath('downloads.log'), 'r') as file:
        for i, line in enumerate(file):
            found = findall(URL_PATTERN, line)
            if len(found) > 0:
                founds.append(found[0])

            if i % 1000 == 0:
                print('At line {}.'.format(i))
    
    with open(path.abspath('visited.json'), 'w') as file:
        json.dump({
            'visited_urls': founds
        }, file)
    
    print('Done')


if __name__ == '__main__':
    main()