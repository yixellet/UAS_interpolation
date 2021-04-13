from config import TELEMETRY, TIMESTAMPS, TRAJECTORY, OUTPUT
from fileToArray import fileToArray
from interpolation import interpolation

trackPoints = open(TRAJECTORY, 'r')
timeStamps = open(TIMESTAMPS, 'r')
telemetry = open(TELEMETRY, 'r')
output = open(OUTPUT, 'w')

trackPointsArray = fileToArray(trackPoints, 0, 2, ',')
timeStampsArray = fileToArray(timeStamps, 10, 7, ' ')
trackPointsArrayModified = []

for line in trackPointsArray:
    newLine = []
    newLine.append(line[0])
    newLine.append(float(line[1]))
    newLine.append(float(line[2]))
    newLine.append(float(line[3]))
    time = []
    for number in line[5].split()[1].split(':'):
        time.append(float(number))
    newLine.append(time)
    trackPointsArrayModified.append(newLine)

timeStampsArrayModified = []

for line in timeStampsArray:
    time = []
    for number in line[0].split():
        time.append(float(number))
    timeStampsArrayModified.append(time)

timeStampsArraySec = []

for line in timeStampsArrayModified:
    seconds = line[0]*3600 + line[1]*60 + line[2]
    timeStampsArraySec.append(seconds)

trackPointsArraySec = []

for line in trackPointsArrayModified:
    newLine = []
    newLine.append(line[0])
    newLine.append(line[1])
    newLine.append(line[2])
    newLine.append(line[3])
    seconds = line[4][0]*3600 + line[4][1]*60 + line[4][2]
    newLine.append(seconds)
    trackPointsArraySec.append(newLine)

interpolatedPoints = []
count = 0

for time in timeStampsArraySec:
    j = 0
    photoPoint = []
    while time > trackPointsArraySec[j][4] and j < len(trackPointsArraySec) - 1:
        j += 1
    lat = interpolation(trackPointsArraySec[j - 1][1], trackPointsArraySec[j][1], trackPointsArraySec[j - 1][4], trackPointsArraySec[j][4], time)
    lon = interpolation(trackPointsArraySec[j - 1][2], trackPointsArraySec[j][2], trackPointsArraySec[j - 1][4], trackPointsArraySec[j][4], time)
    elev = interpolation(trackPointsArraySec[j - 1][3], trackPointsArraySec[j][3], trackPointsArraySec[j - 1][4], trackPointsArraySec[j][4], time)
    photoPoint.append(lat)
    photoPoint.append(lon)
    photoPoint.append(elev)
    interpolatedPoints.append(photoPoint)

count = 1
for point in interpolatedPoints:
    output.write(str(count) + ',')
    for i in point:
        output.write(str(i) + ',')
    output.write('\n')
    count += 1

output.close()
