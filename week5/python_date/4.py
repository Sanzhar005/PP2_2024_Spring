from datetime import datetime
date_format = "%Y-%m-%d %H:%M:%S"
date1_string = input()
date1 = datetime.strptime(date1_string, date_format)

date2_string = input()
date2 = datetime.strptime(date2_string, date_format)

deltatime = date1 - date2
deltatime = deltatime.total_seconds()
print(deltatime)