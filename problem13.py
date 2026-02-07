def min_jumps(arr):
    n = len(arr)

    # If array has only one element, no jump is needed
    if n == 1:
        return 0

    # If first element is 0, we cannot move anywhere
    if arr[0] == 0:
        return -1

    # Initialize variables
    maxReach = arr[0]   # Maximum index that can be reached
    steps = arr[0]      # Steps remaining in current jump
    jumps = 1           # At least one jump is required

    # Traverse the array
    for i in range(1, n):

        # If we have reached the last index
        if i == n - 1:
            return jumps

        # Update the maximum reachable index
        maxReach = max(maxReach, i + arr[i])

        # Use one step
        steps -= 1

        # If no steps are left, we must take another jump
        if steps == 0:
            jumps += 1

            # If current position is beyond maxReach, end is unreachable
            if i >= maxReach:
                return -1

            # Reinitialize steps for the new jump
            steps = maxReach - i

    return -1


# -------- MAIN CODE --------
if __name__ == "__main__":
    # Test cases
    arr1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    arr2 = [1, 4, 3, 2, 6, 7]
    arr3 = [0, 10, 20]

    print("Input:", arr1)
    print("Minimum Jumps:", min_jumps(arr1))  # Output: 3

    print("\nInput:", arr2)
    print("Minimum Jumps:", min_jumps(arr2))  # Output: 2

    print("\nInput:", arr3)
    print("Minimum Jumps:", min_jumps(arr3))  # Output: -1
