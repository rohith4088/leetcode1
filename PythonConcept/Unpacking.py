
#this script talks about the * and ** operators in python

#the * operator is used with lists and tuples and the ** operator is mostly used with dictonoary 
#the * operator is associated with args and the ** is associated with kwargs (keyword arguments)

l1 = [1,2,3]
print(l1)
#the output will be-->[1,2,3]
#if we wish to print the individual element if the list we can do so by the * operator
print(*l1)
#the output will be--> 1 2 3
l2 = [4,5,6]
#we wish to add the individual elements of the l1 and l2 list to list
l3 = [*l1,*l2,"hello"]
print(l3)
#the output willl be --> [1,2,3,4,5,6]
#if we do this

l3 = [l1,l2]
print(l3)
#we get l3 as list within list --> [[1,2,3],[4,5,6]]
#usinf it for *args

def MyFunc(*args):
    for el in args:
        print(el)
MyFunc(2,3,5,5,5,6)#we can pass any number of parameters


#using the ** operator

d1={"a":1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6}
comined_dict = {**d1,**d2}
print(comined_dict)

#using it with **kwargs ,this traets the dictory key:vlaue pair as keyword arguments

def MyFunc1(**kwargs):
    print("the follwing argumemts were passed")
    for k , v in kwargs.items():
        print(f'the key is {k} ')
        print(f"the value is {v}")
MyFunc1(name = 'rohit',age = 32,occupation = 'programmer')

