from datetime import datetime, timedelta

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

# 3. Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")

# 4. Calculate the time difference between now and new year.
new_year = datetime(year + 1, 1, 1)
time_diff = new_year - now

# 5. Calculate the time difference between 1 January 1970 and now.
time_diff_1970 = now - datetime(1970, 1, 1)

# 6. Think, what can you use the datetime module for? Examples:
#    - Time series analysis
#    - To get a timestamp of any activities in an application
#    - Adding posts on a blog 
