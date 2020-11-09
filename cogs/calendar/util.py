from icalendar import Calendar, Event
from datetime import datetime, date, timedelta

CALENDAR_PATH = "Assets/4TC-GR2.ical"
RESPONSE_TEMPLATE = """from {starting_time}:00 to {end_time}:00 :: {course} at  {location}       {details}"""
time = datetime(2020, 11, 9, 8, 0, 2)
day = timedelta(days=1)


def getCourseStartingTime():
    now = datetime.now()
    if 8 < now.hour < 10:
        return datetime(now.year, now.month, now.day, 8, 0, 2)
    elif 10 < now.hour < 12:
        return datetime(now.year, now.month, now.day, 10, 0, 2)
    elif 14 < now.hour < 16:
        return datetime(now.year, now.month, now.day, 14, 0, 2)
    elif 16 < now.hour < 18:
        return datetime(now.year, now.month, now.day, 18, 0, 2)
    else:
        return datetime(now.year, now.month, now.day, 18, 0, 2)


def getCurrentCourse(CalendarPath):
    with open(CalendarPath, 'rb') as calendarFile:
        mCal = Calendar.from_ical(calendarFile.read())
    for component in mCal.walk():
        if component.name == 'VEVENT':
            if component['DTSTART'].dt == datetime.now():
                return component


def getCourseByDate(date=datetime.today().date(),calendarPath=CALENDAR_PATH):
    result = []
    with open(calendarPath, 'rb') as calendarFile:
        mCal = Calendar.from_ical(calendarFile.read())
    for component in mCal.walk():
        if component.name == 'VEVENT':
            if component['DTSTART'].dt.date() == date:
                result.append(component)
                if len(component) == 4:  # optimization
                    break
    return result


def formatResponse(course, template=RESPONSE_TEMPLATE):
    try:
        starting_time = str(course['DTSTART'].dt.hour).zfill(2)
        end_time      = str(course['DTEND'].dt.hour).zfill(2)
        currentCourse = course['SUMMARY']
        location      = "👩‍💻👨‍💻👩‍💻👨‍💻👩‍💻👨‍💻" if ("Distanciel" in course['LOCATION']) else course['LOCATION']
        details       = course['DESCRIPTION']
        return template.format(starting_time=starting_time, end_time=end_time,
                               course=currentCourse, location=location,
                               details=details)
    except:
        return "Error 😞"



