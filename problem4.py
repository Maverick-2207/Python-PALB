def findUnion(a, b):
    # Convert both arrays to sets to remove duplicates
    set_a = set(a)
    set_b = set(b)
    
    # Take union of both sets
    union_set = set_a.union(set_b)
    
    # Convert back to list and return
    return list(union_set)


# Driver code
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(sorted(findUnion(a, b)))
