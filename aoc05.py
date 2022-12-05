import re

def ingest(file1, file2):
    with open(file1, 'r') as f:
        stacks = dict()
        for key, line in enumerate(f):
            stacks[key+1] = line[:-1].split('\t')               # key+1 or it's wrong!

    with open(file2, 'r') as g:
        inst = []
        for h in g:
            temp = [int(_) for _ in re.findall(r'\d+', h)]      # note: \d*  and \d? don't work for this!
            inst.append(temp)
    return stacks, inst


def part_a(stacks, inst):
    for step in inst:
        for i in range(step[0]):
            stacks[step[2]].append(stacks[step[1]].pop())
    return ''.join([v[-1] for v in stacks.values()])


s, i = ingest('in05_stacks.txt', 'in05_inst.txt')
ans_a = part_a(s,i)
print(ans_a)
