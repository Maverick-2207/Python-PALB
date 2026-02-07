# Given array
arr = [2, 3, -8, 7, -1, 2, 3]

# Initialize current sum and maximum sum
current_sum = arr[0]
max_sum = arr[0]

# Traverse the array from the second element
for i in range(1, len(arr)):
    
    # Either extend the previous subarray
    # or start a new subarray from current element
    current_sum = max(arr[i], current_sum + arr[i])
    
    # Update maximum sum if current sum is greater
    max_sum = max(max_sum, current_sum)

# Print the maximum subarray sum
print(max_sum)
