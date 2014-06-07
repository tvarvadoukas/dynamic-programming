""" 
Find the minimum number of coins that sum up to a value.

Description:
Given a list of N coins, their values (V1, V2, ... , VN), and the 
total sum S. Find the minimum number of coins the sum of which is S 
(we can use as many coins of one type as we want), or report that it's 
not possible to select coins in such a way that they sum up to S. 
"""

coins = [3, 4]
target = 100020

values = {}
values[0] = 0
L = [0]
i = 0
solution = True
while True:
    if i == len(L):
        print 'No solution!'
        solution = False
        break   

    cur = L[i]
    if cur == target:
        break
    for c in coins:
        togoin = cur + c
        if togoin > target:
            break

        if togoin not in values:
            values[togoin] = values[cur] + 1
            L.append(togoin)
        else: # is this case possible?!
            values[togoin] = min(values[togoin], values[cur] + 1)
    i = i + 1

if solution:
    print 'Solution is: ', values[target]
