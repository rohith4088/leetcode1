# def InsertionSort(collection):
#     for index in range(1 , len(collection)):
#         while index > 0 and collection[index - 1] > collection[index]:
#             collection[index] , collection[index-1] = collection[index - 1]  , collection[index]
#             index -= 1
#     return collection
# if __name__ == "__main__":
#     user_input = input('Enter numbers separated by a comma:\n').strip()
#     unsorted = [int(item) for item in user_input.split(',')]
#     print(*InsertionSort(unsorted) , sep = ',')



#trying alternate logic just a little change using a temp variable
def insertion_sort(collection):
    for i in range(1 , len(collection)):
        key = collection[i]
        j = i - 1
        while j >= 0 and collection[j] > key:
            collection[j+1] = collection[j]
            j -= 1
        collection[j+1] = key
    return collection

if __name__ == "__main__":
    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*insertion_sort(unsorted) , sep = ',')