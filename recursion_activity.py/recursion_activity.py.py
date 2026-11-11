
# Hands-On Activity: Recursive Array Toolkit
# Name: Januel M Pastorfide

# 1. Sum the array
def sum_array(numbers):
    # Base case
    if len(numbers) == 0:
        return 0

    # Recursive case
    return numbers[0] + sum_array(numbers[1:])


# 2. Find the largest number
def find_largest(numbers):
    # Input rule: Array must not be empty
    if len(numbers) == 0:
        raise ValueError("Array must contain at least one number")

    # Base case
    if len(numbers) == 1:
        return numbers[0]

    # Recursive case
    largest_rest = find_largest(numbers[1:])

    if numbers[0] > largest_rest:
        return numbers[0]
    else:
        return largest_rest


# 3. Count a chosen number
def count_number(numbers, target):
    # Base case
    if len(numbers) == 0:
        return 0

    # Recursive case
    if numbers[0] == target:
        return 1 + count_number(numbers[1:], target)
    else:
        return count_number(numbers[1:], target)


# TESTING THE FUNCTIONS

print("===== RECURSIVE ARRAY TOOLKIT =====")

# Test 1: Sum the array
print("\n1. SUM THE ARRAY")

print("Empty array:", sum_array([]))
print("One number:", sum_array([5]))
print("Several numbers:", sum_array([10, 20, 30]))
print("Positive and negative:", sum_array([10, -5, 3, -2]))


# Test 2: Find the largest number
print("\n2. FIND THE LARGEST NUMBER")

print("One number:", find_largest([8]))
print("Largest at beginning:", find_largest([50, 20, 10, 5]))
print("Largest at end:", find_largest([10, 20, 30, 50]))
print("Negative numbers:", find_largest([-10, -5, -20, -2]))


# Test 3: Count a chosen number
print("\n3. COUNT A CHOSEN NUMBER")

print("Empty array:", count_number([], 5))
print("Target appears several times:", count_number([2, 5, 2, 7, 2], 2))
print("Target does not appear:", count_number([1, 3, 4, 6], 5))
print("Target appears once:", count_number([1, 2, 3], 2))


print("\n===== END OF PROGRAM =====")
