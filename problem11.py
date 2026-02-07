import heapq

# Function to find kth smallest element
def kth_smallest(arr, k):
    # Convert array into a min-heap
    heapq.heapify(arr)

    # Pop elements k-1 times
    for _ in range(k - 1):
        heapq.heappop(arr)

    # The next popped element is the kth smallest
    return heapq.heappop(arr)


# Example 1
arr1 = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k1 = 4
print(kth_smallest(arr1, k1))   # Output: 5

# Example 2
arr2 = [7, 10, 4, 3, 20, 15]
k2 = 3
print(kth_smallest(arr2, k2))   # Output: 7
