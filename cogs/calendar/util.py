from icalendar import Calendar, Event
from datetime import datetime, date, timedelta

CALENDAR_PATH = "cogs/calendar/Assets/4TC2.ical"
RESPONSE_TEMPLATE = """{starting_time}:00 ➡️ {end_time}:00 :: {course} at  {location}  |  {details}"""
COURSE_COMMENT = {"GES1": "😭"}
DETAILS_COMMENT = {"Image": "🏙", "haskell": "😭"}
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


def getCourseByDate(date=datetime.today().date(), calendarPath=CALENDAR_PATH):
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
        starting_time = formatTime(course, 'DTSTART')
        end_time = formatTime(course, 'DTEND')
        currentCourse = formatCourse(course)
        location = formatLocation(course)
        details = formatDetails(course)
        return template.format(starting_time=starting_time, end_time=end_time,
                               course=currentCourse, location=location,
                               details=details)
    except:
        return "Error 😞"


def formatTime(course, time):
    return str(course[time].dt.hour).zfill(2)


def formatCourse(course):
    currentCourse = course['SUMMARY']
    courseName = currentCourse[currentCourse.index('-') + 1:currentCourse.index('/')]
    i = len(currentCourse) - 1
    while i != 0:
        if currentCourse[i] == "/":
            break
        i -= 1
    beginStrip = currentCourse.index('_') if '_' in currentCourse else currentCourse.index('/')
    courseType = currentCourse[beginStrip + 1:i]
    comment = ""
    if courseName in COURSE_COMMENT.keys():
        comment = f" {COURSE_COMMENT[courseName]}"

    return f"{courseName} {courseType}{comment}"


def formatLocation(course):
    if "Distanciel" in course['LOCATION']:
        return "👩‍💻👨‍💻👩‍💻"
    else:
        return course['LOCATION']


def formatDetails(course):
    comment = ""
    description = course['DESCRIPTION']
    for key in DETAILS_COMMENT.keys():
        if key in description:
            comment = f" {DETAILS_COMMENT[key]}"
            break

    return f"{description}{comment}"


tomorrow = datetime.now() + timedelta(days=1)
for c in getCourseByDate(tomorrow.date()):
    print(formatResponse(c))
