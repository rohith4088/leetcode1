# Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps 
# through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

# Properties

# Worst case performance O(n2)
# Best case performance O(n)
# Average case performance O(n2)


def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j] , collection[j+1] = collection[j+1] , collection[j]
        if not swapped : break #break once the collection is fully sorted
    return collection

if __name__ == "__main__":
    user_input = input('Enter numbers separated by a comma:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*bubble_sort(unsorted), sep=',')
            

