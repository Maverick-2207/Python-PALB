# Given array
arr = [1, 2, 3, 4, 5]
n = len(arr)

# Step 1: Store the last element
last = arr[n - 1]

# Step 2: Shift elements one position to the right
for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]

# Step 3: Place last element at the first position
arr[0] = last

# Print the rotated array
print(arr)
# Output: [5, 1, 2, 3, 4]