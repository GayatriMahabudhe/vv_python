#1) Find the maximum and minimum elements in a tuple
def tuple_min_max(t):
    """Return (min_value, max_value) from a tuple without using built-ins like min/max."""
    if not t:
        raise ValueError("Tuple is empty.")

    # Initialize with the first element
    min_val = max_val = t[0]


    for x in t[1:]:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

    return min_val, max_val

data = (5, 2, 9, 3, 7, 1)
mn, mx = tuple_min_max(data)
print("Tuple:", data)
print("Min:", mn, "Max:", mx)


#2) Convert a list of tuples into a dictionary

def list_of_tuples_to_dict(pairs):
    """
    Convert a list of 2-element tuples into a dictionary.
    If duplicate keys exist, later ones overwrite earlier ones (like dict behavior).
    """
    result = {}
    for k, v in pairs:
        result[k] = v
    return result
pairs = [("Aarav", 95), ("Isha", 82), ("Aarav", 97)]
converted = list_of_tuples_to_dict(pairs)
print("List of tuples:", pairs)
print("Dictionary:", converted)

#3) Count the occurrence of an element in a tuple without using built-in methods
def count_in_tuple(t, target):
    """Count how many times 'target' appears in tuple t, without using t.count()."""
    count = 0
    for x in t:
        if x == target:
            count += 1
    return count
data = (1, 2, 3, 2, 2, 4, 1)
print("Tuple:", data)
print("Count of 2:", count_in_tuple(data, 2))
print("Count of 1:", count_in_tuple(data, 1))
print("Count of 5:", count_in_tuple(data, 5))

#4) Create a tuple with mutable elements and modify the mutable data inside it

def modify_mutable_in_tuple():
    # Tuple containing lists (lists are mutable)
    t = ([1, 2, 3], ["a", "b"], [10, 20])
    print("Original tuple:", t)

    # Modify inner lists (allowed because lists are mutable)
    t[0][0] = 99          # change first element of first list
    t[1].append("c")      # append to second list
    t[2].extend([30, 40]) # extend third list

    print("Modified tuple:", t)

modify_mutable_in_tuple()

#5) Swap two tuples
def swap_tuples(a, b):
    """Swap two tuples and return them in swapped order."""
    a, b = b, a
    return a, b
t1 = (1, 2, 3)
t2 = ("x", "y")
print("Before swap:", t1, t2)
t1, t2 = swap_tuples(t1, t2)
print("After swap: ", t1, t2)
