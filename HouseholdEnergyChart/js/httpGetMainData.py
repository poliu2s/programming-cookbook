#Author: Po Liu
#Date: April 2, 2013

# This script sends an HTTP GET request to access the feed
#
# Requires installation of requests library in Python which can be found at
# http://docs.python-requests.org/en/latest/

import requests
import re
import csv
from datetime import datetime
import datetime
import calendar
import time

#Main Loop
while(1):
	#HTTP Request with necessary headers
    Main1weekPerHour = requests.get("https://api.cosm.com/v2/feeds/69392/datastreams/0.csv?duration=1week&interval=3600seconds&limit=168",
                        headers={"X-ApiKey" : "B9bdBfmvz-ECW03fIFuVio7oOYiSAKxvVTg0ZEQza1Fjbz0g"})

    dataRaw = Main1weekPerHour.text
    dataLines = re.split('\n', dataRaw)

	#Parse the date from energy, iteratively break down into lists
	#containing year, month, day, hour, energy of each data point
    dateAndEnergyList = []
    for i in range(len(dataLines)):
        dateAndEnergyList.append(re.split('T', dataLines[i]))


    date = []
    timeAndEnergy = []
    for i in range(len(dateAndEnergyList)):
        date.append(dateAndEnergyList[i][0])
        timeAndEnergy.append(dateAndEnergyList[i][1])


    timeM = []
    energy = []
    timeAndEnergyList = []
    for i in range(len(timeAndEnergy)):
        timeAndEnergyList.append(re.split(',', timeAndEnergy[i]))
        timeM.append(timeAndEnergyList[i][0])
        energy.append(timeAndEnergyList[i][1])

    wheelEnergyString = ""
    for i in range(len(energy)):
        if (i+1 < len(energy)):
            wheelEnergyString += "{title: " + date[i] + ", value: " + energy[i] + "}, "
        else:
            wheelEnergyString += "title: " + date[i] + ", value: " + energy[i] + "}"



    # Find the day of the week that each datapoint was recorded
    dateList = []
    year = []
    month = []
    day = []
    weekday = []
    for i in range(len(date)):
        dateList.append(re.split('-', date[i]))
        year.append(dateList[i][0])
        month.append(dateList[i][1])
        day.append(dateList[i][2])
        weekday.append(datetime.datetime(int(year[i]),int(month[i]),int(day[i]),0,0,0,0).weekday())

    # Determine the hour recorded of each datapoint
    timeList = []
    hour = []
    for i in range(len(timeM)):
        timeList = re.split(':', timeM[i])
        hour.append(timeList[0])

    wheelHourString = ""
    for i in range(24):
        if (int(hour[0])+i < 24):
            wheelHourString += str(int(hour[0])+i) + ":00\", \""

        else:
            wheelHourString += str(int(hour[0])+i-24) + ":00\", \""

    weekdayMap = list(calendar.day_abbr)
    wheelWeekdayString = ""
    for i in range(7):
        if (weekday[0]+i> 6):
            weekday[0] -= 7
        if (i < 6):
            wheelWeekdayString += "\"" + weekdayMap[weekday[0]+i] + "\","
        else:
            wheelWeekdayString += "\"" + weekdayMap[weekday[0]+i] + "\""
        
        


    # Add .js code
    data = "var data = [];\n"
    for i in range(len(energy)):
        data += "data[" + str(i) + "] = {title: \"" + str(date[i]) + "\", value: " + energy[i] + "};\n"
    data += 'var chart = circularHeatChart()\n' + \
        'chart.innerRadius(20)\n' + \
        '.segmentHeight(20)\n' + \
        '.range([\"white\", \"steelblue\"])\n' + \
        '.radialLabels([' + wheelWeekdayString + '])\n' + \
        '.segmentLabels([\"' + wheelHourString + '"]);\n' + \
        'chart.accessor(function(d) {return d.value;})\n' + \
        'd3.select(\'#chart3\')' + \
        '.selectAll(\'svg\')\n' + \
        '.data([data])\n' + \
        '.enter()\n' + \
        '.append(\'svg\')\n' + \
        '.call(chart);\n\n' + \
        'd3.selectAll(\"#chart3 path\").on(\'mouseover\', function() {\n' + \
        'var d = d3.select(this).data()[0];\n' + \
        'd3.select("#info").text(\'On \' + d.title + \', power demand was \' + d.value + \'W.\');\n' + \
        '});\n\n' + \
        'd3.selectAll(\"#chart3 svg\").on(\'mouseout\', function() {\n' + \
        'd3.select(\"#info\").text(\'\');\n' + \
        '});'




    # Write out
    myFile = open('mainEnergy.js', 'w')
    myFile.write(data)
    myFile.close()

    #Update interval
    time.sleep(36000)





