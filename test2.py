import time, datetime

str = "2017-08-27"
date = datetime.datetime.strptime(str, "%Y-%m-%d")
print(date)

str1 = date.strftime("%Y-%m-%d")
print(str1)