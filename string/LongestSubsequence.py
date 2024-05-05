#topics--> string , set , sliding window
#time complexity = O(n)
#memory complexity = O(n)
def LongestSubsequence(s:str)-> int:
    charset = set()
    res =0
    l = 0
    for r in range(len(s)):
        while s[r] in charset: #is the right element is inthe set then
            charset.remove(s[l])#w remove the left element from the set
            l += 1
        charset.add(s[r])
        res = max(res,r-l+1)
    return res
string = "abcabcbb"
print(LongestSubsequence(string))