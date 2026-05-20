import datetime
import time
import schedule

def task():
    print("Task after each minute executed.")
    print("Current time is: ", datetime.datetime.now())

#Entry point of script
def main():
    print("Inside main function")
    print("Scheduler start...")
    schedule.every(1).minutes.do(task)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Starter of main application
if __name__ == "__main__":
    main()
