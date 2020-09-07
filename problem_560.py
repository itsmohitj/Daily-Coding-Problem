#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Solution:

#Loop through the array. For ith element, if k-arr[i] is present in the array, then it will return True.

def find_pairs(arr,k):
    for i in range(len(arr)):
        if k-arr[i] in arr:
            return True
    return False


if __name__ == '__main__':
    print("Enter List:\n")
    arr=list(map(int,input().split()))
    k=int(input("Enter value of k: "))
    print(find_pairs(arr,k))
