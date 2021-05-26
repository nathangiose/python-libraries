from datetime import datetime, timedelta, date
dt = date.today()
for i in range(10):
    dt = dt + timedelta(days=14)
    print(dt)
