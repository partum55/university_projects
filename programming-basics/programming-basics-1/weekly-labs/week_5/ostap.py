sequence = [1,2,3,1,1,1,2]
counter = 1
for n in range(1, len(sequence)+1):
    for k in range(len(sequence)):
        try:
            if sequence[:n] == sequence[(k*n)+n:(k*n)+(2*n)]:
                counter += 1
                pattern = sequence[:n]
        except IndexError:
            pass
    if len(pattern) > 0 and len(sequence)/len(pattern) != counter:
        pattern= []
        counter = 1

print((pattern, counter))
