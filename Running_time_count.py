# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time

def count(n):
    units=2+n  # 1 for print "in a clique...",1 for for j in range(n) and n times for i in range(j)
    for i in range(n):
        units+=i     #each time (j-1) print statements..,j from 0 to n-1
    return units

def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j




