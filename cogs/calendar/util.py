import os
import requests
from icalendar import Calendar, Event
from datetime import datetime, date, timedelta
import time
from prettytable import PrettyTable

CALENDAR_PATH = "cogs/calendar/Assets/4TC2.ical"
WEEKDAYS = {1: "Lundi", 2: "Mardi", 3: "Mercredi", 4: "Jeudi", 5: "Vendredi"}
RESPONSE_TEMPLATE = """{starting_time}:00 ➡️ {end_time}:00 :: {course} at  {location}  |  {details}"""
COURSE_COMMENT = {"GES1": "😭", "CNA": "😢"}
DETAILS_COMMENT = {"Image": "🏙", "haskell": "😭"}
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


def getCourseByDate(promptDate=datetime.now().date(), calendarPath=CALENDAR_PATH):
    result = []
    with open(calendarPath, 'rb') as calendarFile:
        mCal = Calendar.from_ical(calendarFile.read())
    for component in mCal.walk():
        if component.name == 'VEVENT':
            if component['DTSTART'].dt.date() == promptDate:
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


def downloadCalendar():
    URL_TEMPLATE = "http://tc-net2.insa-lyon.fr/aff/AffichageEdtPalmGroupe.jsp?promo={year}&groupe={group}&dateDeb=1604856847608"
    ASSETS_DIR = "cogs/calendar/Assets"
    YEARS = ["3", "4", "3A", "4A", "5"]
    GROUPS = range(1, 4)

    for year in YEARS:
        for group in GROUPS:
            if "A" in year and group in [2, 3]:
                continue
            DownloadURL = URL_TEMPLATE.format(year=year, group=group)
            formatedGrpName = group if not "A" in year else "A"
            formatedYearName = year if not "A" in year else year[0]
            fileName = f"{formatedYearName}TC{formatedGrpName}.ical"
            filePath = os.path.join(ASSETS_DIR, fileName)

            r = requests.get(DownloadURL)

            with open(filePath, "wb") as f:
                f.write(r.content)

            time.sleep(1)  # to not overload tc-net servers


def getWeekCalendar(calendarPath=CALENDAR_PATH, offset=0):
    """ @HBA
    compute the week calendar of a group
    :param calendarPath: path to the calendar file of the group
    :param offset: int to offset the calendar week
    :return: Table Object that can be printed
    """
    CurrentWeekday = datetime.today().isoweekday()
    WeekCalendar = {}
    for DayIndex in range(0, CurrentWeekday):
        Day = datetime.today() - timedelta(days=DayIndex) + timedelta(days=offset * 7)
        WeekCalendar[CurrentWeekday - DayIndex] = getCourseByDate(promptDate=Day.date(), calendarPath=calendarPath)
    for DayIndex in range(CurrentWeekday, 6):
        Day = datetime.today() + timedelta(days=DayIndex + 1 - CurrentWeekday) + timedelta(days=offset * 7)
        WeekCalendar[DayIndex + 1] = getCourseByDate(promptDate=Day.date(), calendarPath=calendarPath)

    for DayIndex in range(1, 7):
        formattedCourses = []
        is4HourCourse = False
        for courseBeginingTime in [8, 10, 14, 16]:
            if is4HourCourse:
                is4HourCourse = False
                continue
            isChanged = False
            for course in WeekCalendar[DayIndex]:
                if course['DTSTART'].dt.hour == courseBeginingTime:
                    if course['DTEND'].dt.hour - course['DTSTART'].dt.hour == 4:
                        formattedCourses += [formatCourse(course)] * 2  # add 4 hour course twice
                        is4HourCourse = True
                    else:
                        formattedCourses.append(formatCourse(course))
                    isChanged = True
                    break
            if not isChanged:
                formattedCourses.append("🥳")
        WeekCalendar[DayIndex] = formattedCourses
        # if len(WeekCalendar[DayIndex]) < 4:
        #     while len(WeekCalendar[DayIndex]) != 4:
        #         WeekCalendar[DayIndex].append("🥳")

    Calendar = PrettyTable()
    for DayIndex in range(1, 6):
        Calendar.add_column(WEEKDAYS[DayIndex], WeekCalendar[DayIndex])

    return Calendar


def getOffset(InputOffset):
    Offset = 0
    if InputOffset[0] == "+":
        Offset = int(InputOffset[1:])
    if InputOffset[0] == "-":
        Offset = - int(InputOffset[1:])
    if InputOffset == "+0" and datetime.today().isoweekday() in [6, 7]:
        Offset = 1
    return Offset