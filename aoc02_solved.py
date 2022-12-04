SCORE = {'X': 1, 'Y': 2, 'Z':3}
OUTCOME = {'X': 0, 'Y': 3, 'Z': 6}

def ingest(file):
    with open(file, 'r') as f:
        a = [_.split(' ') for _ in f.read()
                                    .replace('A', 'X')
                                    .replace('B', 'Y')
                                    .replace('C', 'Z')
                                    .split('\n')][:-1]
    return a


def round_a(them, me):
    temp = SCORE[me]
    if them == me:
        return temp + 3
    if them == 'X':                 # them = rock
        if me == 'Y':               # me = paper
           return temp + 6
        else:                       # me = scissors
            return temp
    if them == 'Y':                 # them = paper
        if me == 'Z':                # me = scissors
            return temp + 6
        else:                       # me = rock
            return temp
    if them == 'Z':                 # them = scissors
        if me == 'X':               # me = rock
            return temp + 6
        else:                       # me = paper
            return temp


def part_a(lst):
    temp = 0
    for each in lst:
        temp += round_a(each[0], each[1])
    return temp


def round_b(them, me):
    temp = OUTCOME[me]
    if me == 'Y':
        return temp + SCORE[them]  # draw, so i pick what they pick

    if me == 'Z':  # I win
        if them == 'X':  # they = Rock so i pick paper
            return temp + SCORE['Y']
        elif them == 'Y':  # they = Paper so i pick scissors
            return temp + SCORE['Z']
        else:  # they = Scissors so I pick rock
            return temp + SCORE['X']

    if me == 'X':  # I lose
        if them == 'X':  # they = Rock so i pick scissors
            return temp + SCORE['Z']
        elif them == 'Y':  # they = Paper so i pick rock
            return temp + SCORE['X']
        else:  # they = Scissors so I pick paper
            return temp + SCORE['Y']

def part_b(lst):
    temp = 0
    for each in lst:
        temp += round_b(each[0], each[1])
    return temp


lst = ingest('in02.txt')
ans_a = part_a(lst)
print(ans_a)
ans_b = part_b(lst)
print(ans_b)
