from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    print("Running APScheduler task...")

def job2():
    print("Running APScheduler task 2...")


scheduler = BlockingScheduler()

# Run every 5 minutes
scheduler.add_job(job, 'interval', minutes=1)

# Run at specific time daily
scheduler.add_job(job2, 'cron', hour=0, minute=4)

scheduler.start()
