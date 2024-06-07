import numpy as np

original_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3  

sublists = np.array_split(original_list, n)
sublists = [list(arr) for arr in sublists if len(arr) == 3 ]  

# Print each sublist individually
for i, sublist in enumerate(sublists):
    print(f"Sublist {i+1}: {sublist}")
