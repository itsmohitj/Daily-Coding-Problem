"""
This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

def isIsomorphic(s,t):
    h1 = {}
    h2 = {}
    for i in range(len(s)):
        if s[i] in h1:
            if h1[s[i]] != t[i]:
                return False
        elif t[i] in h2:
            return False
        else:
            h1[s[i]] = t[i]
            h2[t[i]] = s[i]
    return True


if __name__ == '__main__':
    s1,t1 = "abc", "bcd"
    s2,t2 = "foo", "bar"
    print(isIsomorphic(s1,t1))
    print(isIsomorphic(s2,t2))

# Time Complexity = O(n)
# Space Complexity = O(n)
