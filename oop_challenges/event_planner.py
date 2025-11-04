import datetime as dt

class EventPlanner:
    def __init__(self, year):
        self.year = int(year)
        self.events = {}

    def add_event(self, when, details):
        if when.date() < dt.date.today() or when.year != self.year:
            raise Exception('Invalid Date')
        self.events[when] = details

    def remove_event(self, when):
        if when in self.events:
            del self.events[when]

    def list_events(self):
        print(f'\nEvents in {self.year}')
        for date_time, details in self.events.items():
            print(date_time.strftime('%d %B, %A %Y, %I:%M'))
            print('Details:', details)

year = input('Enter Year : ')
planner = EventPlanner(year)


date = [int(x) for x in input('Enter Date dd/mm/yyyy: ').split('/')]
time = [int(x) for x in input('Enter Time hr:min ').split(':')]

when = dt.datetime(date[2], date[1], date[0], time[0], time[1])
details = input('Details of Event')
planner.add_event(when, details)

print(planner.events)

