"""
Dynamic programming solution unbounded  Knapsack.
"""

# (value, weight) of each item
I = [(0.5, 1), (4, 3), (3, 2)]
MAX = 5 # max weight

# Create a table of [0, 1, .., Ith] X [0, 1, ..., MAX]
V = {}
V[0] = [0] * (MAX+1)

for i in range(1, len(I) + 1):
    V[i] = [0] * (MAX+1)
    for w in range(MAX + 1):
        vj, wj = I[i - 1]

        if w - wj < 0:
            V[i][w] = V[i-1][w]
            continue

        lim = w / wj 
        V[i][w] = V[i-1][w]
        for k in range(1, lim + 1):
            V[i][w] = max(V[i-1][w - k*wj] + k*vj, V[i][w])

for i in range(len(I)+1):
    print str(i) + ' | ', 
    for w in range(MAX+1):
        print str(V[i][w]) + '\t', 
    print ""
