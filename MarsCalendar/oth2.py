# Define 'global' variables
dayOfWeekDict = { 5 : "mon", 6 : "tue", 0 : "wed", 1 : "thu", 2 : "fri", 3 : "sat", 4 : "sun" }


inputYear = int(raw_input("Year: \n"))
inputMonth = int(raw_input("Month: \n"))
inputDay = int(raw_input("Day: \n"))


# TODO: Catch invalid years, months, days

numMonthsInYear = 10
numDaysInWeek = 7
numDaysInMonth = 31

# Loop through days from epoch till input date
iterYear = 1900
iterMonth = 0
iterDayOfMonth = 0
countDaysSinceEpoch = 0
while ( iterYear != inputYear and iterMonth != inputMonth and iterDayOfMonth != inputDay):
    countDaysSinceEpoch += 1

    # Why Month - Check if year is divisible by 6
    if iterYear % 6 == 0:
        numMonthsInYear = 11
    else:
        numMonthsInYear = 10

    # 30 day in month exceptions for Feb and Jun
    if (iterMonth == 1 or iterMonth == 5):
        numDaysInMonth = 30

    # Sept has 32 days on even years
    elif(iterYear % 2 == 0 and iterMonth == 8):
        numDaysInMonth = 32
    else:
        numDaysInMonth = 31

    # Increment iteration days to count through the calendar
    if iterDayOfMonth <= numDaysInMonth:
        iterDayOfMonth += 1
    elif iterMonth <= numMonthsInYear:
        # Reset the days of month because rolled over to new month
        iterDayOfMonth = 0
    else:
        # Reset iterDate because year has rolled over to new year
        iterYear += 1
        iterMonth = 0
        iterDayOfMonth = 0



# # Derived values
# numDaysInYear = numMonthsInYear * numDaysInMonth

# diffYear = inputYear - 1900
# diffMonth = inputMonth - 1   #in case epoch changes
# diffDays = inputDay - 1
#
# # Calculate the number of days between input and epoch
# daysSinceEpoch = (numDaysInYear * diffYear) + (numDaysInMonth * diffMonth) + (diffDays)



# Get the day of week
dayOfWeek = countDaysSinceEpoch % numDaysInWeek

print dayOfWeek
print dayOfWeekDict[dayOfWeek]
