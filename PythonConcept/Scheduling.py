from schedule import repeat , run_pending , every
import time

#using a decorator
# @repeat(every(1).seconds)
# def job():
#     print("i will print every second")
# while True:
#     run_pending()
#     time.sleep(1)


#passing arguments to the schdeuler

@repeat(every(2).seconds,"mars")
@repeat(every(1).seconds,'earth')
def JobTwo(planet):
    print("hello",planet)


while True:
    run_pending()