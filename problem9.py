# Given array and target
nums = [2, 7, 11, 15]
target = 9

# Dictionary to store number and its index
num_index = {}

# Traverse the array
for i in range(len(nums)):
    # Calculate the required number
    complement = target - nums[i]

    # Check if complement already exists in dictionary
    if complement in num_index:
        # If found, print indices
        print([num_index[complement], i])
        break

    # Store current number with its index
    num_index[nums[i]] = i
