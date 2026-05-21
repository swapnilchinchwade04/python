import schedule
import time

def job():
    print("Running scheduled task...")

# Run every 10 seconds
schedule.every(10).seconds.do(job)

# Run daily at 9:00 AM
schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
