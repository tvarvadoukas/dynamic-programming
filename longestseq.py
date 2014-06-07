""" 
Given a sequence of N numbers - A[1] , A[2] , ..., A[N] . 
Find the length of the longest non-decreasing sequence. 

NOTE: not consecutive elements necessarily
"""

L = [5, 3, 4, 8, 6, 7]
#L = [5, 3, 4, 8, 1, 2]

state = []
prev  = []
state.append(1)
prev.append(0)

curmax = 1
curmaxpos = 0

for i in range(1, len(L)):
    state.append(1)
    prev.append(i)
    for j in range(i):
        if L[j] < L[i]:
            if state[j] + 1 > state[i]:
                state[i] = state[j] + 1
                prev[i] = j

    if state[i] > curmax:
        curmax = state[i]
        curmaxpos = i

# Print max subsequence.
print 'Max subsequence has length of: ', curmax
print 'In reversed order: ',
pos = curmaxpos
while True:
    print L[pos],
    if pos == prev[pos]: 
        break
    pos = prev[pos]
print ""
