# Program to display calendar of the given month and year and save your appointments to a text file
print("Program to print the calender of a specific month")

# importing calendar module
import calendar

yy = 2000 # year
mm = 1    # month

yy=int(input("Enter the year"))
mm=int(input("Enter the month's number"))
print(calendar.month(yy, mm))
