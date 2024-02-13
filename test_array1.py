import timeit

def largest_word(s):
    s = s.split()
    
    length = {}
    for i in range(len(s)):
        if s[i].isalpha():
            length[s[i]] = len(s[i])
    max_length = max(length.values())
    for word, length in length.items():
        if length == max_length:
            print(word)

# Test case 1
s1 = "Hello world"
print("Test case 1:")
print("Input:", s1)
print("Output:")
print(timeit.timeit(lambda: largest_word(s1), number=10000))

# Test case 2
s2 = "This is a test"
print("Test case 2:")
print("Input:", s2)
print("Output:")
print(timeit.timeit(lambda: largest_word(s2), number=10000))