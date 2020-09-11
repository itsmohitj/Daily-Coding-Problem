"""
This problem was asked by Jane Street.

Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

a + b = M
a XOR b = N
"""


def plusXorPairs(m,n):
    count=0
    for i in range(1,m):
        a=i
        b=m-a
        if(a^b==n):
            count+=1
    return count

print(plusXorPairs(11,11))

# Time Complexity = O(m)
# Space Complexity = O(1)
