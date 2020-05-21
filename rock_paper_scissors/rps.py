#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    outcome = []
    plays = ['rock', 'paper', 'scissors']

    def find_outcome(rounds_left, result=[]):
        print('RESULT', result)
        if rounds_left == 0:
            print('APPEND', result)
            outcome.append(result)
            print('OUTCOME', outcome)
            return
        for play in plays:
            print('\n')
            print('PLAY', play)
            find_outcome(rounds_left - 1, result + [play])

    find_outcome(n, [])
    print('\nOUTCOME', outcome)
    return outcome

# [
#   ['rock', 'rock'],
#   ['rock', 'paper'],
#   ['rock', 'scissors'],

#   ['paper', 'rock'],
#   ['paper', 'paper'],
#   ['paper', 'scissors'],

#   ['scissors', 'rock'],
#   ['scissors', 'paper'],
#   ['scissors', 'scissors']
# ]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
