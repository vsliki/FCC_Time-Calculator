def add_time(start, duration, arg=None):
  #print("start time: " + str(start))
  #print("duration: " + duration)
  # --- Days of the week -------
  dot = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
    "Sunday"
  ]

  # -------- CLEANING ARG -----------
  if arg != None:
    new_arg = arg.lower()
    new_new_arg = new_arg.capitalize()
    arg = new_new_arg
    #print(arg, dot.index(arg))
    index = dot.index(arg)

  # ----- CLEANING DATA --------

  # sorting hours minutes and day time
  ti = start.split(':')
  time = ti[1].split()
  #print(time)

  minutes = int(time[0])
  hours = int(ti[0])
  daytime = time[1]

  if daytime == "PM":
    hours = int(hours) + 12

  # ------ CLEANING THE  DURATION ------
  duti = duration.split(':')
  du_hours = int(duti[0])
  du_minutes = int(duti[1])

  # ----- COMPUTING THE TIME ----------------

  new_min = minutes + du_minutes
  new_hours = hours + du_hours

  while new_min > 59:
    new_hours = new_hours + 1
    new_min = new_min - 60

  day = 0
  while new_hours >= 24:
    day += 1
    if arg != None:
      index += 1
    new_hours = new_hours - 24

  # ------ SETTING FINAL DAYTIME ---------
  if (new_hours > 12) & (new_hours < 24):
    new_hours = new_hours - 12
    new_daytime = "PM"
  elif new_hours == 24:
    new_hours = new_hours - 12
    new_daytime = "AM"
  elif new_hours == 12:
    new_daytime = "PM"
  else:
    new_daytime = "AM"

  # ------ SETTING FINAL DAY -----------
  if arg != None:
    while index > 6:
      index = index - 7
    arg = dot[index]

  # -------------- PRINT ----------------
  if new_hours == 0:
    new_hours = 12

  if arg == None:
    #print 0 for min digits
    if new_min < 10:
      if day == 0:
        new_time = str(new_hours) + ":0" + str(new_min) + " " + str(
          new_daytime)
      elif day == 1:
        new_time = str(new_hours) + ":0" + str(new_min) + " " + str(
          new_daytime) + " (next day)"
      else:
        new_time = str(new_hours) + ":0" + str(new_min) + " " + str(
          new_daytime) + " (" + str(day) + " days later)"

    else:
      if day == 0:
        new_time = str(new_hours) + ":" + str(new_min) + " " + str(new_daytime)
      elif day == 1:
        new_time = str(new_hours) + ":" + str(new_min) + " " + str(
          new_daytime) + " (next day)"
      else:
        new_time = str(new_hours) + ":" + str(new_min) + " " + str(
          new_daytime) + " (" + str(day) + " days later)"

  else:
    if new_min < 10:
      if day == 0:
        new_time = str(new_hours) + ":0" + str(new_min) + " " + str(
          new_daytime) + ", " + arg
      elif day == 1:
        new_time = str(new_hours) + ":0" + str(new_min) + " " + str(
          new_daytime) + ", " + arg

      else:
        new_time = str(new_hours) + ":0" + str(new_min) + " " + str(
          new_daytime) + ", " + arg + " (" + str(day) + " days later)"

    else:
      if day == 0:
        new_time = str(new_hours) + ":" + str(new_min) + " " + str(
          new_daytime) + ", " + arg
      elif day == 1:
        new_time = str(new_hours) + ":" + str(new_min) + " " + str(
          new_daytime) + ", " + arg + " (next day)"
      else:
        new_time = str(new_hours) + ":" + str(new_min) + " " + str(
          new_daytime) + ", " + arg + " (" + str(day) + " days later)"

  return new_time