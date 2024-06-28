# algorithm that divides the **input list into two part**s: **the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. 
# Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), 
# and moving the sublist boundaries one element to the right.**
# - Worst case performance O(n)^2
# - Best case performance O(n)^2
# - Average case performance O(n)^2
def selection_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i+1 , length):
            if collection[k] < collection[least]:
                least = k
        collection[least] , collection[i] = (collection[i] , collection[least])
    return collection
if __name__ == "__main__":
    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*selection_sort(unsorted) , sep = ',')