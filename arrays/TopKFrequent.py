def TopFreqElements(nums: list[int], k: int) -> list[int]:
    map = {}
    for n in nums:
        if n in map:
            map[n] += 1
        else:
            map[n] = 1
    sorted_el = sorted(map.items() , key = lambda x : (-x[1] , x[0]))
    top = [el for el , _ in sorted_el[:k]]
    return top
nums = [1,1,1,12,1,3,11,34,4,2,233]
k = 2
print(TopFreqElements(nums, k))

