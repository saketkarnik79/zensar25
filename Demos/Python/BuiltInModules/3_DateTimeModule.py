import datetime

#today = datetime.date.today()
# today = datetime.datetime.now()
# print(today)
# print(f"year: {today.year}")
# print(f"month: {today.month}")
# print(f"day: {today.day}")

birthday = datetime.date(2011, 10, 4)
print(f"Birthday: {birthday}")
formatted_birthday = birthday.strftime("%d-%m-%Y")
print(f"Formatted Birthday: {formatted_birthday}")