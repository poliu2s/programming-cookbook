
inputYear = int(raw_input("Year: \n"))
inputMonth = int(raw_input("Month: \n"))
inputDay = int(raw_input("Day: \n"))


# TODO: Catch invalid years, months, days

numMonthsInYear = 10
numDaysInWeek = 7
numDaysInMonth = 31

# Derived values
numDaysInYear = numMonthsInYear * numDaysInMonth

diffYear = inputYear - 1900
diffMonth = inputMonth - 1   #in case epoch changes
diffDays = inputDay - 1

# Calculate the number of days between input and epoch
daysSinceEpoch = (numDaysInYear * diffYear) + (numDaysInMonth * diffMonth) + (diffDays)

# Get the day of week
dayOfWeek = daysSinceEpoch % numDaysInWeek

dayOfWeekDict = { 5 : "mon", 6 : "tue", 0 : "wed", 1 : "thu", 2 : "fri", 3 : "sat", 4 : "sun" }

print dayOfWeekDict[dayOfWeek]
