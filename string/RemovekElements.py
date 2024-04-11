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