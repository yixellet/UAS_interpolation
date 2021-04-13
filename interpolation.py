def interpolation(prevVal, nextVal, prevTime, nextTime, photoTime):
    deltaLat = nextVal - prevVal
    deltaTime = nextTime - prevTime
    deltaTimeX = photoTime - prevTime
    deltaLatX = deltaLat * deltaTimeX / deltaTime
    photoLat = prevVal + deltaLatX
    return photoLat