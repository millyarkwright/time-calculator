
def add_time(start, duration, day=''):
  print('-----START-----')
  print(start, duration, day)
  
  days_week = [
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
    'sunday'
  ]

  period_switch = {'AM': 'PM', 'PM': 'AM'}

  # Split out start and duration times and period
  time, start_period = start.split()
  start_hours, start_minutes = [int(i) for i in time.split(':')]
  duration_hours, duration_minutes = [int(i) for i in duration.split(':')]

  hours = start_hours + duration_hours
  minutes = start_minutes + duration_minutes
  days_later = 0
  dayofweek, day_later_string, new_period = [''] * 3
  # dayofweek = ""
  # day_later_string = ""
  # new_period = ""

  # If minutes are >= 60, shift minutes to hour
  if minutes >= 60:
    hours = hours + (minutes // 60)  # // floor division (rounds the result down to the nearest whole number)
    minutes = minutes % 60  # Returns the remaining minutes (after dividing the minutes by 60). Eg if minutes was 70, this would change to 10.

  # If hours is greater than 24, shift hours to days.
  if hours >= 24:
    days_later += (hours // 24)
    hours = hours % 24

  # print('hours:', hours)
  # print('minutes', minutes)
  # print('days_later', days_later)

  # Period Change - If the starting hour was <= 11 (aka in the AM) and the new hour is > 11 (aka has passed into the PM), switch the period
  if (start_hours <= 11) and (hours > 11):
    new_period = period_switch[start_period]
    if start_period == 'PM' and new_period == 'AM':
    # if (start_period, new_period) == ('PM','AM'):
      days_later += 1
    # As we've added a day and changed the period, we can divide the hours by 12 and return the remainder (hours).
    if hours > 12:
      hours = hours % 12

  # print('-----NEXT-----')
  # print('hours:', hours)
  # print('minutes', minutes)
  # print('days_later', days_later)
  # print('new_period', new_period)
  # print('----------')

  # Find the day of the week n days later. Need to do % len(days_week) so it the day_index doesn't got beyond the length of the array.
  if day:
    day_index = (days_week.index(day.lower()) + days_later) % len(days_week)
    dayofweek = f", {days_week[day_index].title()}"
    # print('DAYOFWEEK', dayofweek)

  if days_later == 1: 
    day_later_string = " (next day)"  
  elif days_later > 1:
    day_later_string = f" ({days_later} days later)"

  new_time = f"{hours}:{str(minutes).rjust(2,'0')} {new_period or start_period}{dayofweek}{day_later_string}"

  print(new_time)
  
  return new_time
