from schedule import repeat , run_pending , every
import time

import schedule
#using a decorator
# @repeat(every(1).seconds)
# def job():
#     print("i will print every second")
# while True:
#     run_pending()
#     time.sleep(1)


#passing arguments to the schdeuler

# @repeat(every(2).seconds,"mars")
# @repeat(every(1).seconds,'earth')
# def JobTwo(planet):
#     print("hello",planet)


# while True:
#     run_pending()

import schedule

def greet(name):
    print('Hello {}'.format(name))

schedule.every().day.do(greet, 'Andrea').tag('daily-tasks', 'friend')
schedule.every().hour.do(greet, 'John').tag('hourly-tasks', 'friend')
schedule.every().hour.do(greet, 'Monica').tag('hourly-tasks', 'customer')
schedule.every().day.do(greet, 'Derek').tag('daily-tasks', 'guest')

friends = schedule.get_jobs('friend')