"""
This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""

def allOccurrences(string,substring):
    res=[i for i in range(len(string)) if string.startswith(substring,i)]
    return res

print(allOccurrences("abrabrabrab","abrab"))

# Time Complexity = O(n)
# Space Complexity = O(n)
