# Write a list comprehension that creates a list of numbers from 1 to 20 that
# are divisible by 3.
div_by_3 = [i for i in range(1, 21) if i % 3 == 0]
print(div_by_3)

# Create a dict {"a": 97, "b": 98, ... } using comprehension. Use ord built-in
# to obtain ASCII code and string.ascii_lowercase to get all letters.
import string

ascii_dict = {char: ord(char) for char in string.ascii_lowercase}
print(ascii_dict)

# Write a nested set comprehension to flatten a nested list [[1, 2, 3, 4],
# [4, 5, 6, 7], [6, 7, 8, 9]] -> {1, 2, 3, 4, 5, 6, 7, 8, 9}.

nested_list = [[1, 2, 3, 4], [4, 5, 6, 7], [6, 7, 8, 9]]
flat_set = {item for sublist in nested_list for item in sublist}

# Write a nested list comprehension to transpose a 3x3 matrix (switch its rows
# and columns).
matrix = [
    [4, 6, 8],
    [0, 0, 0],
    [1, 2, 3],
]

transposed_matrix = [[matrix[i][j] for i in range(3)] for j in range(3)]
print(transposed_matrix)