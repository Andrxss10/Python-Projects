#PYTHON PROGRAM FOR DAYS OF THE WEEK BY INPUT

week = ["monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"]

day = str(input("Enter the day of the week: ")).lower()

if day in week:
    print(f"The day you enrolled was: {day}")
else:
    print("Non-existent day of the week")
