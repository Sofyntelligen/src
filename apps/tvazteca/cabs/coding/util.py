from datetime import datetime


def subString(string: str, char: chr):
    number = string.index(char)
    string = string[number + 1:]
    return string


def getDate():
    date = datetime.now()
    day = int(date.day)
    month = int(date.month)
    year = int(date.year)
    return completeNumber(str(day)) + '/' + completeNumber(str(month)) + '/' + str(year)


def getTime():
    date = datetime.now()
    hour = int(date.hour)
    minute = int(date.minute)
    second = int(date.second)

    return completeNumber(str(hour)) + '/' + completeNumber(str(minute)) + '/' + completeNumber(str(second))


def getDateBoorlandActual(date):
    days = int(date.strftime("%j"))
    year = int(date.year)
    boorland = 0
    count = 0

    for x in range(1900, year):
        count += 1
        if count == 4:
            count = 0
            boorland += 366
        else:
            boorland += 365

    boorland += days

    return (boorland + 1)


def optionMux(mux: int):
    value = mux
    if value == 1:
        mux = 'D2MUX'
    elif value == 2:
        mux = 'DTP'
    else:
        mux = 'NE'

    return mux


def converterBytes(number):
    B = float(number)
    KB = float(1024)
    MB = float(KB ** 2)
    GB = float(KB ** 3)
    TB = float(KB ** 4)

    if B < KB:
        return '{0} {1}'.format(B, 'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)


def formmatDate(date):
    date_array = date.split('-')
    date_temporary = datetime(int(date_array[2]), int(date_array[1]), int(date_array[0]))
    date = getDateBoorlandActual(date_temporary)

    return date


def formattTimeSecond(time: int):
    seconds = ((time / 32) - 1) * 60
    hours = int(seconds / 3600)
    minutes = int((seconds % 3600) / 60)
    second = int(seconds % 60)

    return completeNumber(str(hours)) + ':' + completeNumber(str(minutes)) + ':' + completeNumber(str(second))


def formattTimeMinute(time: int):
    seconds = time / 1000
    hours = int(seconds / 3600)
    minutes = int((seconds % 3600) / 60)
    second = int(seconds % 60)

    return completeNumber(str(hours)) + ':' + completeNumber(str(minutes)) + ':' + completeNumber(str(second))


def completeNumber(number):
    if len(number) == 1:
        number = '0' + number

    return number


def completeNumberAnyone(number):
    number_string = ''
    for x in range(len(str(number)), 4):
        number_string += '0'
    number_string += str(number)
    return number_string


def convertToSecond(hour: int, minute: int, second: int):
    hour = hour * 3600
    minute = minute * 60
    time = second + minute + hour + 60
    time = time * 32
    time = time / 60

    return int(time)
