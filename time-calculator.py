
def add_time(start, duration, day=''):

  """
    Required parameters:
      * a start time in the 12-hour clock format (ending in AM or PM) 
      * a duration time that indicates the number of hours and minutes
    Optional parameter:
      * (optional) a starting day of the week, case insensitive
    
    Function will add the duration time to the start time and return the result.

    Examples: 
      add_time("3:00 PM", "3:10")
      Returns: 6:10 PM

      add_time("11:30 AM", "2:32", "Monday")
      Returns: 2:02 PM, Monday

      add_time("6:30 PM", "205:12")
      Returns: 7:42 AM (9 days later)
    
  """


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

  # If minutes are >= 60, shift minutes to hour
  if minutes >= 60:
    hours = hours + (minutes // 60)  # '//' = floor division (rounds the result down to the nearest whole number)
    minutes %= 60  # Returns the remaining minutes (after dividing the minutes by 60)

  # If hours is greater than 24, shift hours to days.
  if hours >= 24:
    days_later += (hours // 24)
    hours = hours % 24

  # Period Change if start hours and hours are on either side of the 12 threshold (hours can be on the 12 threshold).
  if (start_hours <= 11) and (hours > 11):
    new_period = period_switch[start_period]
  # Only increase days_later if period went from PM to AM. AM to PM isn't a new day.
    if start_period == 'PM' and new_period == 'AM':
      days_later += 1
    # 12 hours is the equivalent to 1 period and as we've changed ('increased') the period, we can 'reduce' the hours. 
    if hours > 12:
      hours %= 12

  # Find the day of the week n days later. Modulus operator to cycle through the days_week array.
  if day:
    day_index = (days_week.index(day.lower()) + days_later) % len(days_week)
    dayofweek = f", {days_week[day_index].title()}"

  if days_later == 1: 
    day_later_string = ' (next day)'  
  elif days_later > 1:
    day_later_string = f" ({days_later} days later)"

  new_time = f"{hours}:{str(minutes).rjust(2,'0')} {new_period or start_period}{dayofweek}{day_later_string}"

  # print(new_time)
  
  return new_time
