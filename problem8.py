# Given sorted array and target
nums = [1, 3, 5, 6]
target = 5

# Initialize pointers
left = 0
right = len(nums) - 1

# Binary Search
while left <= right:
    mid = (left + right) // 2

    # If target is found, return its index
    if nums[mid] == target:
        print(mid)
        break

    # If target is greater, search in right half
    elif nums[mid] < target:
        left = mid + 1

    # If target is smaller, search in left half
    else:
        right = mid - 1
else:
    # If target is not found,
    # left will be the correct insert position
    print(left)
