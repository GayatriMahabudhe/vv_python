#1) Remove duplicate elements from a list without using set
def remove_duplicates(lst):
    """Return a new list with duplicates removed, preserving original order."""
    result = []
    for item in lst:
        if item not in result:  # only add if not already present
            result.append(item)
    return result

data = [1, 2, 2, 3, 1, 4, 3, 5, 5]
print("Original:", data)
print("Without duplicates:", remove_duplicates(data))

#2) New list containing only even numbers using list comprehension
def filter_even(numbers):
    """Return a list of even numbers using list comprehension."""
    return [n for n in numbers if n % 2 == 0]
nums = [10, 11, 12, 13, 14, 15, 16]
print("Original:", nums)
print("Even numbers:", filter_even(nums))

#3) Find the second largest element in a list
def second_largest(lst):
    """
    Return the second largest distinct element in the list.
    Raises ValueError if not enough distinct elements.
    """
    if len(lst) < 2:
        raise ValueError("List must have at least two elements.")

    # Remove duplicates while preserving order
    unique = []
    for x in lst:
        if x not in unique:
            unique.append(x)

    if len(unique) < 2:
        raise ValueError("List must have at least two distinct elements.")

    # Find largest and second largest in one pass
    largest = second = None
    for x in unique:
        if (largest is None) or (x > largest):
            second = largest
            largest = x
        elif (second is None or x > second) and x != largest:
            second = x


#4) Create a nested list and calculate the sum of each inner list
def sum_inner_lists(nested):
    """Return a list where each element is the sum of the corresponding inner list."""
    return [sum(inner) for inner in nested]
nested_list = [
    [1, 2, 3],
    [10, 20],
    [5],
    [7, 8, 9, 10]
]
print("Nested list:", nested_list)
print("Sum of each inner list:", sum_inner_lists(nested_list))

#5) Demonstrate shallow copy vs deep copy with mutable elements

import copy

def demonstrate_copies():
    original = [[1, 2], [3, 4], [5, 6]]
    print("Original:", original)

    # Shallow copy: copies the outer list, but inner lists are shared
    shallow = original[:]
    deep = copy.deepcopy(original)
    original[0][0] = 99

    print("\nAfter modifying original[0][0] = 99")
    print("Original:", original)
    print("Shallow copy (affected):", shallow)  # inner lists shared -> change visible
    print("Deep copy (not affected):", deep)    # fully independent -> unchanged

    # Modify the outer list structure
    original.append([7, 8])
    print("\nAfter appending a new inner list to original")
    print("Original:", original)
    print("Shallow copy:", shallow)  # shallow not auto-updated; separate outer list
    print("Deep copy:", deep)        # deep not auto-updated; separate outer list
demonstrate_copies()



