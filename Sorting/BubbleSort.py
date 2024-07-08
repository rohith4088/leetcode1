# Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps 
# through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

# Properties

# Worst case performance O(n2)
# Best case performance O(n)
# Average case performance O(n2)


# def bubble_sort(collection):
#     length = len(collection)
#     for i in range(length - 1):
#         swapped = False
#         for j in range(length - 1 - i):
#             if collection[j] > collection[j+1]:
#                 swapped = True
#                 collection[j] , collection[j+1] = collection[j+1] , collection[j]
#         if not swapped : break #break once the collection is fully sorted
#     return collection

# if __name__ == "__main__":
#     user_input = input('Enter numbers separated by a comma:').strip()
#     unsorted = [int(item) for item in user_input.split(',')]
#     print(*bubble_sort(unsorted), sep=',')
            



# #implemention bubble sort cause i keep forgeting bubble sort
# from memory_profiler import profile

# file = open("BubbleSortUsage.txt" , 'w+')

# @profile(stream = file)
# def Bubble(collection):
#     length = len(collection)
#     for i in range(length - 1):
#         swapped = False
#         for j in range(length - 1 - i): # the length - i - 1 has one less iteration with every i outer pass, this esnures less checking becaus the last element is guranted to be sorted.
#             if collection[j] > collection[j+1]:
#                 swapped = True
#                 collection[j] , collection[j+1] = collection[j+1] , collection[j]
#         if not swapped : break # break once the whole collection is sorted
#     return collection

# if __name__ == "__main__":
#     unsorted = [5,4,3,2,1]
#     print(*Bubble(unsorted),sep = ',')

# #[1,2,3,2,4,4]

from memory_profiler import profile

file = open("BubbleLessOptimised.txt" , 'w+')

@profile(stream = file)
def Bubble(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1): #less optimised code because it checks till the last element unnecessarily , when we can strongly assume that the last element is already sorted.
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j] , collection[j+1] = collection[j+1] , collection[j]
        if not swapped : break
    return collection

if __name__ == "__main__":
    unsorted = [5,4,3,2,1]
    res = Bubble(unsorted) 
    print(res)
    #print(next(res))
