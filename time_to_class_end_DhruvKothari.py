from datetime import datetime

currentTime = datetime.now()

classEndTime = datetime(year=2025, month=2, day=11, hour=14, minute=19, second=0, microsecond=0)

time = classEndTime-currentTime
print(time)

