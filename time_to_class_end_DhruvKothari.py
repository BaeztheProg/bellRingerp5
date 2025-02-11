from datetime import datetime

currentTime = datetime.now()

classEndTime = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=14, minute=19, second=0, microsecond=0)

time = classEndTime-currentTime
time = time.seconds
time = time/60

print(time)
