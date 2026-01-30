def kthSmallest(arr, k):
    # Sort the array in ascending order
    arr.sort()
    
    # Return the element at index k-1
    return arr[k-1]


# Driver code
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
print(kthSmallest(arr, k))
