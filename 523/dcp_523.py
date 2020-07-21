def plusXorPairs(m,n):
    count=0
    for i in range(1,m):
        a=i
        b=m-a
        if(a^b==n):
            count+=1
    return count

print(plusXorPairs(11,11))
