#THE DIAMOND PROBLEM THAT COMES WITH MULTIPLE INHERIITANCE
'''
 A
/\
B C
\ /
 D
'''

#the __mro__ (method resolution order) (new style)
#The mro uses the C3 linearization technique for method resolution order

class A(object) : x = 'c'
class B(A) : pass
class C(A) : r ='v'
class D(B , C) : pass
D.r
D.__mro__


#POTENTIAL BUG CAUSED BY MULTIPLE INHERITANCE AND ITS SOLUTION

