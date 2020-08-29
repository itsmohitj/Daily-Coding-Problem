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
