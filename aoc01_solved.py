def ingest(file):
    with open(file, 'r') as f:
        a = f.read()
        #print(a)
        b = a.split('\n\n')
       # print(b)
        c =[]
        for each in b:
           # temp = each.split('\n')
            c.append(sum([int(_) for _ in
                                  each.splitlines()]))
            
       # a = [_[:-1] for _ in f]    
    return c

t = ingest('in01.txt')
ans = sum(sorted(t, reverse=True)[:3])
print(ans)