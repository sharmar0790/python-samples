import time

a = time.localtime()
if 6 < a.tm_hour < 18:
    print("It's Day Time")
else:
    print("It's Night time")
