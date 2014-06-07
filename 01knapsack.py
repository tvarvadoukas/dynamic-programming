"""
Dynamic programming solution to 0/1 Knapsack.
"""

# (value, weight) of each item
I = [(10, 5), (40, 4), (30, 6), (50, 3)]
MAX = 10 # max weight

# (value, weight) of each item
I = [(1, 1), (4, 3), (3, 2)]
MAX = 4 # max weight

# Create a table of [0, 1, .., Ith] X [0, 1, ..., MAX]
V = {}
V[0] = [0] * (MAX+1)

for i in range(1, len(I) + 1):
    V[i] = [0] * (MAX+1)
    for w in range(MAX + 1):
        vj, wj = I[i - 1]
        if w >= wj:
            V[i][w] = max(V[i-1][w-wj] + vj, V[i-1][w])
        else:
            V[i][w] = V[i-1][w]

for i in range(len(I)+1):
    print str(i) + ' | ', 
    for w in range(MAX+1):
        print str(V[i][w]) + '\t', 
    print ""
