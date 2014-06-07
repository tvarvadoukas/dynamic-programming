"""
You are given a list of integer numbers [a1, a2, ..., an] 
and are required to find the subarray with the maximum sum 
that doesn't contain consecutive elements.

Expected complexity: O(N)

Example input:
[2, 5, 6, 5, 3]

Example output:
11

Explanation:
2 + 6 + 3
"""
def find_max_sum(v):
    S = [0] * len(v)
    S[0] = v[0]
    S[1] = v[1]
    for i in range(2, len(v)):
        if v[i] <= 0:
            S[i] = max(max(S[:i-1]), v[i])
        else:
            S[i] = max(max(S[:i-1]) + v[i], v[i])
    print max(S)

# 11
v = [2, 5, 6, 5, 3]

# 168
v = [4, 5, 17, 3, 12, 29, 0, -25, 25, 28, 16, 16, 16, 11, -10, -4, 3, -25, 10, -20, 1, -9, 23, 13, -25, 9, -24, 15, 5, -20]
find_max_sum(v)
