def MergeAlternative(word1:str,word2:str)->str:
    res = ''
    min_length = min(len(word1),len(word2))
    for i in range(min_length):
        res += word1[i] + word2[i]
    if len(word1) > len(word2):
        res += word1[min_length:]
    else:
        res += word2[min_length:]
    return res
word1 = 'rohit'
word2 = 'hello'
print(MergeAlternative(word1,word2))