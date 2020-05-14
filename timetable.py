import datetime

def Timetable():
    now=datetime.datetime.now()
    time = now.time()
    now = now.weekday()
    nownow=now
    if now==1 or now == 5 or now == 6:
        return '''
Свобода\n'''
    if now == 0:
        if nownow==now and int(time.strftime("%H")) * 60 + int(time.strftime("%M")) > 20 * 60 + 5:
            now += 1
        else:
            return '''Расписание на понедельник\n\n
История механики\n
12:30 - 14:05\n
16-24\n\n
Спецкурс\n
15:00 - 16:35\n
12-06\n\n
Кафедральный семинар\n
16:45 - 18:20\n
12-25\n\n
Курс написания научных статей\n
18:30 - 20:05\n
12-25\n'''
    if now == 2:
        if nownow==now and int(time.strftime("%H")) * 60 + int(time.strftime("%M")) > 14 * 60 + 5:
            now += 1
        else:
            if datetime.strftime('%j')-51 % 14 == 0:
                return '''Расписание на среду\n\n
    Экономика\n
    10:45 - 12:20\n
    16-22\n\n
    Философия\n
    12:30 - 14:05\n
    13-06\n'''
            else:
                return '''Расписание на среду\n\n
Философия\n
10:45 - 12:20\n
16-22\n\n
Философия\n
12:30 - 14:05\n
13-06\n'''
    if now == 3:
        if nownow==now and int(time.strftime("%H")) * 60 + int(time.strftime("%M")) > 12 * 60 + 20:
            now += 1
        else:
            return '''Расписание на четверг\n\n
Экономика\n
10:45 - 12:20\n
12-24\n'''
    if now == 4:
        if nownow==now and int(time.strftime("%H")) * 60 + int(time.strftime("%M")) > 12 * 60 + 20:
            return '''
Свобода\n'''
        else:
            return'''Расписание на пятницу\n\n
История механики\n
10:45 - 12:20\n
16-24\n'''

