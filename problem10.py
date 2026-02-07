# Given array
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)

# If array has only one element, no jumps needed
if n == 1:
    print(0)

# If first element is 0, cannot move anywhere
elif arr[0] == 0:
    print(-1)

else:
    # maxReach: farthest index we can reach
    maxReach = arr[0]

    # steps: steps remaining in current jump
    steps = arr[0]

    # jumps: number of jumps taken
    jumps = 1

    # Traverse array
    for i in range(1, n):
        
        # If we have reached the end
        if i == n - 1:
            print(jumps)
            break

        # Update maxReach
        maxReach = max(maxReach, i + arr[i])

        # Use a step to move
        steps -= 1

        # If no steps left
        if steps == 0:
            jumps += 1

            # If current index is beyond maxReach, cannot move
            if i >= maxReach:
                print(-1)
                break

            # Re-initialize steps
            steps = maxReach - i
