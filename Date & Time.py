from datetime import datetime, date, time, timedelta
import time as tm

# Current datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Creating specific dates
birthday = datetime(2003, 6, 07, 08, 30)
print(birthday.date())
print(birthday.time())

# Date arithmetic
future = now + timedelta(days=7, hours=3)
diff = future - now
print(diff.days)

# Parsing dates
date_str = "2026-06-19"
parsed = datetime.strptime(date_str, "%Y-%m-%d")

# Timestamp
timestamp = now.timestamp()
converted_back = datetime.fromtimestamp(timestamp)

# Sleep
print("Start")
tm.sleep(1)         # Pause 1 second
print("End")
