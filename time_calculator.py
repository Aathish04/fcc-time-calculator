def add_time(start, duration, day=""):
  startday=", "+day.upper().capitalize()
  start=start.replace(" ",":").split(":")
  starthour=int(start[0])
  startminute=int(start[1])
  meridian=start.pop()
  
  starthour+=12 if meridian=="PM" else 0 #Convert to 24 Hour.
  
  duration=duration.replace(" ",":").split(":")
  durationhour=int(duration[0])
  durationminute=int(duration[1])

  endminute=durationminute+startminute
  if endminute>=60:
    durationhour+=endminute//60
    endminute%=60
  endhour=starthour + durationhour #Get the ending hour. (24)
  
  durationhour%=24 # Set to number of hours in the last day.
  
  days_past=endhour//24
  endhour %= 24

  if (endhour//12) %2 ==0 and durationhour > 0:
    meridian="AM" if meridian=="PM" else "PM"
  
  if endhour > 12:
    endhour%=12
    meridian="PM" if meridian=="AM" else meridian
  elif endhour == 12:
    meridian="AM" if meridian=="PM" else "PM"
  elif endhour ==0:
    endhour+=12

  if len(day)>0:
    days=[", Sunday",", Monday",", Tuesday",", Wednesday",", Thursday",", Friday",", Saturday"]
    curr_day_index=days.index(startday)
    fin_day_index=curr_day_index+days_past
    if fin_day_index>=7:
      fin_day_index %=7

    day=days[fin_day_index]

  if days_past==1:
    daytext=" (next day)"
  elif days_past!=0:
    daytext=f" ({days_past} days later)"
  else:
    daytext=""
  outstring=f'{endhour}:{endminute:02} {meridian}{day}{daytext}'
  return outstring