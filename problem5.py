def findLargest(arr):
    # Assume first element is largest
    largest = arr[0]
    
    # Traverse through the array
    for num in arr:
        
        # If current number is greater than largest
        if num > largest:
            largest = num
            
    return largest


# Driver code
arr = [1, 8, 7, 56, 90]
print(findLargest(arr))
