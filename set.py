#1) Union, Intersection, Difference, Symmetric Difference of two sets

def set_operations(a, b):
    """
    Return a tuple with (union, intersection, difference_a_b, difference_b_a, symmetric_difference)
    """
    union_set = a | b                 # or a.union(b)
    intersection_set = a & b          # or a.intersection(b)
    difference_a_b = a - b            # elements in a not in b
    difference_b_a = b - a            # elements in b not in a
    sym_diff_set = a ^ b              # or a.symmetric_difference(b)
    return union_set, intersection_set, difference_a_b, difference_b_a, sym_diff_set

# --- Demo ---
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
u, i, d_ab, d_ba, sd = set_operations(A, B)
print("A:", A, "B:", B)
print("Union:", u)
print("Intersection:", i)
print("Difference A-B:", d_ab)
print("Difference B-A:", d_ba)
print("Symmetric difference:", sd)

#2) Remove common elements from two sets

def remove_common_in_place(a, b):
    """
    Removes common elements from both sets in-place.
    After this, a and b will have only their unique elements.
    """
    common = a & b
    a.difference_update(common)
    b.difference_update(common)

# --- Demo ---
A = {1, 2, 3, 4}
B = {3, 4, 5}
remove_common_in_place(A, B)
print("A (no commons):", A)  # {1, 2}
print("B (no commons):", B)  # {5}


#3) Check whether one set is a subset of another

def is_subset(a, b):
    """Return True if set a is subset of set b."""
    return a <= b  # or a.issubset(b)

A = {1, 2}
B = {1, 2, 3, 4}
print("Is A subset of B?", is_subset(A, B))  # True
print("Is B subset of A?", is_subset(B, A))  # False


#4) Iterate over a set and print only elements greater than a given number

def print_greater_than(s, threshold):
    """Print elements in set s that are strictly greater than threshold."""
    for x in s:
        if x > threshold:
            print(x)

S = {5, 1, 9, 3, 7}
print("Elements > 4:")
print_greater_than(S, 4)

#5) Convert a list with duplicates → set → back to list with unique elements

def unique_list_from_list(lst):
    """
    Convert list to set (to remove duplicates) and back to list.
    Order will be arbitrary because sets are unordered.
    """
    return list(set(lst))

data = [1, 2, 2, 3, 1, 4, 3, 5, 5]
unique_list = unique_list_from_list(data)
print("Original:", data)
print("Unique (order not guaranteed):", unique_list)
