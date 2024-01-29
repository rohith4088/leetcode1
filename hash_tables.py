### HASHTABLES
##Hash Tables are data structures which generally provide very fast(O(1)) lookups, insertions and deletions
#In Python, dictionaries are implemented as hash tables.
#The way hashing works is that there is a bucket containing slots to fill with elements.
#Like in arrays, elements are referenced by their integer indexes, in dictionaries, or hash tables,
#values are referenced by their keys, which can be of any data type.
#Now there are different kinds of hash functions (eg: MD5, SHA1, SHA256) which are used to convert the keys into hashes, which are unique for each key
#And the hashes are then mapped to some slot in the bucket. And the key and value pair get stored in the slot,
#or in some accompanying data structure within the slot (like, linked lists)

#In general, the lookup, insert and delete operations all are very fast, in the order of O(1)
#But in some cases, more than one keys can map to the same slot and that increases the time complexity by some margin,
#although not by a lot in most cases. This is known as a collision.
#Now, like for almost all problem there is some sort of a solution in the computer science world,
#collisions can also be resolved by numerous collision resolution techniques like open addressing and closed addressing

#Enough details, let's look at how hash tables are implemented in Python using dictionaries.
#Data ais stored in an associative manner 
#applications
# to prevent sensitive data, such as web analytics, passwords, and payment details.
# To encrypt information exchange between browsers and web servers, and create session IDs for data caching and internet applications.
# To find identical data through lookup functions.
# Adding a digital signature to an email.


#what is the need
#using list
stock_prices = []
f = open("stock_prices.csv",'w+')
f.write("march 9,320,march 10, 340,march 11 , 350,march 31,450")
f.close()
stock_prices = []
with open("stock_prices.csv",'r') as f:
    for line in f:
        tokens = line.split()
        day = tokens[0]
        prices = tokens[1]
        stock_prices.append([day,prices])
print(stock_prices)
#retrieval can prove inefficent for largeer datasets
for element in stock_prices:
    if element[0] == "march 31":
        print(element[1])
 
 #using dictionary
stock_prices = {}
with open("stock_prices.csv",'r') as f:
    for line in f:
        tokens = line.split()
        day = tokens[0]
        prices = tokens[1]
        stock_prices[day] = prices #key:value
print(stock_prices)

for element in stock_prices:
    if element[0] == "march 31":
        print(element[1])
# the retreival becomes very fast O(1)
#first step in creating a hasmap is defining a hash function
#hash function is a function that takes a string and returns a number
#this can be achieved by many methods one of whihc is using ascii

def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100
get_hash("march 6") 



class HashTables:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    def __deleteitem__(self,key):
        h = get_hash(key)
        self.arr[h] = None
t = HashTables()
t.add("march 6",140)
t.get('march 6')
del t['march 6']
#this does not handel collsion
#t['march 6'] = 130 is more convineient to write than to call get add function
# to override this python provides __setitem__() and __getitem__() whihch overrides this sytnax

t['march 7'] = 340
t['march 7']



#handling collsions using seperate chaining method or linear probing


