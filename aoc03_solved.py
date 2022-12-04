def part_a(file):
    total = 0
    with open(file, 'r') as f:
        for u in f:
            x = list(set(list(u)[:len(u) // 2]) & set(list(u)[len(u) // 2:]))[0]
            if x.isupper():
                total += ord(x) - 38
            else:
                total += ord(x) - 96
    return total


def part_b(file):
    total = 0
    with open(file, 'r') as f:
        u = f.read().split('\n')
        u = u[:-1]
        print(u)
        groups = len(u)//3
        for i in range(groups):
            j = i * 3
            x = list(set(list(u)[j]) & set(list(u)[j+1]) & set(list(u)[j+2]))[0]
            if x.isupper():
                total += ord(x) - 38
            else:
                total += ord(x) - 96
    return total


a = part_a('in03.txt')
print(a)
b = part_b('in03.txt')
print(b)
