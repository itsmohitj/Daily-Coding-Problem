def allOccurrences(string,substring):
    res=[i for i in range(len(string)) if string.startswith(substring,i)]
    return res

print(allOccurrences("abracadabra","abra"))
