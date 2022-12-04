def ingest(file):
    a = []
    with open(file, 'r') as f:
        for line in f:
            a.append(line[:-1].split(','))
    return a


def mk_range(item):
    temp = [int(_) for _ in item.split('-')]
    return set(range(temp[0], temp[1]+1))


def parts(listing):
    part_a = 0
    part_b = 0
    for pair in listing:
        a = mk_range(pair[0])
        b = mk_range(pair[1])
        if a.issubset(b) or b.issubset(a):
            part_a += 1
        if len(a & b) > 0:
            part_b +=1
    return part_a, part_b



listing = ingest('in04.txt')
a, b = parts(listing)
print(f'part a:   {a}')
print(f'part b:   {b}')
