from gdata.calendar.service import CalendarService

calService = CalendarService("user", "pass")
calService.ProgrammaticLogin()
calUrl = None
for cal in calService.GetCalendarListFeed().entry:
    if cal.title.text == 'm.0.m.':
        calUrl = cal.link[0].href

for event in calService.GetCalendarEventFeed(calUrl).entry:
    print event.id.text
