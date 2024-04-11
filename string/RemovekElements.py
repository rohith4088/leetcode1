#the algorithm used is called the monotonic stack
#the idea is to keep a stack that is always in increasing order
#when we see a number that is less than the top of the stack, we pop the 
#top of the stack and decrement k
#we keep doing this until k is 0 or the stack is empty
#then we add the current number to the stack
#finally we remove the last k elements from the stack and return the result
#the time complexity is O(n) and the space complexity is O(n)
#this is because we only iterate through the string once and we use a stack

def RemoveKElements(num,k):
    stack = []
    for c in num:
        while k > 0 and stack and stack[-1] > c:
            k -= 1
            stack.pop()
        stack.append(c)
    stack = stack[:len(stack) - k]
    res = ''.join(stack).lstrip('0')
    return res if res else '0'

print(RemoveKElements('1432219',3))