# import threading
# import time
# flag = False
# def worker():
#     counter = 0
#     while True:
#         time.sleep(1)
#         counter += 1
#         print(counter)
# threading.Thread(target = worker,daemon = True).start()
# input("press enter to quit")
# flag = True


from threading import Thread
class InputReader(Thread):
    def run(self):
        self.line_of_text = input()
print("enetr some value and press enter")
thread = InputReader()
thread.start()
count = result = 1
while thread.is_alive():
    result = count+count
    count += 1
print("calculated squares upto {0} * {0} = {1}".format(count,result))
print("while you typed {}".format(thread.line_of_text))
