import datetime
import time
import winsound
time=eval(input("enter the time hh:mm:ss"))

while True:
    current_time=datetime.datetime.now().strftime("%H:%M:%S")
    if current_time==time:
        winsound.Beep(500,500)
        break
