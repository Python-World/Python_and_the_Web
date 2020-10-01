import time

unix_timestamp = int(input())
utc_time = time.gmtime(unix_timestamp)
print(time.strftime("%m/%d/%Y %I:%M%p (UTC)", utc_time))
