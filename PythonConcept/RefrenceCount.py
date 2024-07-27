


import sys

x = object()
print(sys.getrefcount(x))

y = x

print(sys.getrefcount(x))

del y
print(sys.getrefcount(x))
