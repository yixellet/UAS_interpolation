from config import TELEMETRY, TIMESTAMPS, TRAJECTORY, OUTPUT

def fileToArray(file: str, divider: str):
    """
    Преобразует содержимое файла в массив
    """
    tempArr = []
    for line in file:
        point = []
        for prop in line[:-1].split(divider):
            point.append(prop)
        tempArr.append(point)
    return tempArr
f = open(TIMESTAMPS, 'r')
print(fileToArray(f, '  '))