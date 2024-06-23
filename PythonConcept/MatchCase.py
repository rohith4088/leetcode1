class Point:
    def __init__(self , x, y):
        self.x = x
        self.y = y
def where_is(point):
    match point:
        case Point(x = 0,y = 0):
            return "you are at the origin"
        case Point(x = 0,y =1):
            return "you are the y co-ordinate"
        case _:
            return "god knows"
    
p = Point(0,12)
print(where_is(p))