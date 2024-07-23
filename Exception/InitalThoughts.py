# def Ex(number):
#     if number == 0:
#         raise ValueError("**The Number Cannot Be Zero**")
#     elif number % 2:
#         raise ValueError("**The Number Cannot Be An Odd Number**")
#     else:
#         print(f"the number is {number}")
# # Ex(2)
# # Ex(3)
# Ex(0)


class EvenOnly(list):
    def append(self , integer):
        if not isinstance(integer , int):
            raise TypeError("the value should be an interger")
        if integer % 2:
            raise ValueError("the number should be an even number")
        super().append(integer)

e = EvenOnly()
#e.append(1)
e.append(2)
#e.append(3)
e.append(4)
#e.append(5)
print(e)
