from datetime import datetime
date1 = input("Enter first date (dd-mm-yyyy): ")
date2 = input("Enter second date (dd-mm-yyyy): ")
d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")
months = (d2.year - d1.year) * 12 + (d2.month - d1.month)
if months == 1 and d1.day == d2.day:
    print("Exactly 1 Month Apart")
elif months < 1:
    print("Less Than 1 Month Apart")
else:
    print("More Than 1 Month Apart")
