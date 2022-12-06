def parts(file, part_a):
    with open(file, 'r') as f:
        a = f.read()
        a = list(a)
        b = []
        if part_a: 
            digits = 4 
        else:
            digits = 14
        for _ in range(digits):
            b.append(a.pop(0))
        i = digits
        while len(b) != len(set(b)):
            b.pop(0)
            b.append(a.pop(0))
            i += 1
            
        return i
        
        
t = parts('in06.txt', False)
print(t)