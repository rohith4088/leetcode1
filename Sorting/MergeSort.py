#Merge Sorrt is a divide and conquer method 
def MergeSort(collection):
    if collection is None:
        return None
    if len(collection) <= 1:
        return collection
    length = len(collection)
    if length > 1:
        midpoint = length // 2
        left_half = MergeSort(collection[:midpoint])
        right_half = MergeSort(collection[midpoint:])
        i = 0 #for the left half
        j = 0 #for the right half
        k = 0 #for the main collection
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] =  left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1

            while i < left_length:
                collection[k] = left_half[i]
                i += 1
                k += 1
            while j < right_length:
                collection[k] = right_half[j]
                j += 1
                k += 1
        return collection
    
collection = [1,3,2,4,34,2,1,2,3,4,3]
print(MergeSort(collection))