def minimize_height_difference(arr, k):
    n = len(arr)

    # Sort the array
    arr.sort()

    # Initial difference without any modification
    ans = arr[n - 1] - arr[0]

    # Smallest and largest after first modification
    smallest = arr[0] + k
    largest = arr[n - 1] - k

    # Traverse middle elements
    for i in range(1, n):
        # If decreasing makes height negative, skip
        if arr[i] - k < 0:
            continue

        # Possible new min and max
        current_min = min(smallest, arr[i] - k)
        current_max = max(largest, arr[i - 1] + k)

        # Update answer
        ans = min(ans, current_max - current_min)

    return ans


# Example 1
arr1 = [1, 5, 8, 10]
k1 = 2
print(minimize_height_difference(arr1, k1))  # Output: 5

# Example 2
arr2 = [3, 9, 12, 16, 20]
k2 = 3
print(minimize_height_difference(arr2, k2))  # Output: 11
