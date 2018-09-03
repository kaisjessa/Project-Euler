days_of_week = "sun mon tue wed thu fri sat".split()
year = 1900
month = 0 #January
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0
days = day
day_week = days_of_week[0]

count = 0

while(year < 2001):
	day += 1
	days += 1
	if(day > months[month]):
		day = 1
		month += 1
	if(month > 11):
		month = 0
		year += 1
	day_week = days_of_week[days % 7]
	if(day_week== "sun" and day==1 and year >= 1901):
		count += 1
print(count)