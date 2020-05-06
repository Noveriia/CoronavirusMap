import schedule
import time

def do_nothing():
    print("Steven Marsh")

schedule.every(10).seconds.do(do_nothing)
schedule.every().day.at('01:00').do(do_nothing())
while 1:
    schedule.run_pending()
    time.sleep(1)