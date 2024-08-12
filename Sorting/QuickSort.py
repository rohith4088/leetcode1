def QuickSort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection[0]
        greater = [element for element in collection[1:] if element > pivot]
        lesser = [element for element in collection[1:] if element < pivot]
        return QuickSort(lesser) + [pivot] + QuickSort(greater)

collection = [3,21,4,1,23,5,2,1]
print(*QuickSort(collection),sep = ',')