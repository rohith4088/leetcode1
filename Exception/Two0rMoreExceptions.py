# #DOING SAME THINGS WITH DIFFRERNT EXCEPTIONS
# def divisor(num):
#     try:

#         if num == 13:
#             print("13 is an unlucky number")
#         return 100 / num
#     except (TypeError , ZeroDivisionError):
#         return "enter a number more thnan zero or enter a valid number"
# for val in (0 , "hello" , 50.0 , 13):
#     print("testing {}".format(val))
#     print(divisor(val))



# #HANDLING EACH EXCEPTION IN A DIFFRERNT WAY

def divisor2(num):
    try:
        if num == 13:
            raise ValueError("no no not 13")
    except ZeroDivisionError:
        print("enetr a number other than 0")
    except TypeError:
        print("enter a vaild number")
    except ValueError:
        print("13 s an unlucky number")
        raise

