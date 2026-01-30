def findMinMax(arr):
    # Assume first element is both minimum and maximum
    min = arr[0]
    max = arr[0]
    
    # Traverse through each element in the array
    for num in arr:
        
        # If current number is smaller than minimum
        if num < min:
            min = num
            
        # If current number is greater than maximum
        if num > max:
            max = num
    
    # Return result as a list
    return [min, max]


# Driver code
arr = [1, 4, 3, 5, 8, 6]
print(findMinMax(arr))
