# Given an array with n elements and an integer k. Divide the array into subarrays, each of them containing k elements.For example: 
# Input: arr[]={1, 32, 5, 6, 9, 3} and k=2

# The subarrays will have elements:
# {1,32}, {5,6}, {9,3}.

def divide_array(arr,k):
    n = len(arr)
    sub = []
    for i in range(0,n,k):
        arrs = arr[i:i+k]
        sub.append(arrs)
    return sub
print(divide_array([1, 32, 5, 6, 9, 3],2))
