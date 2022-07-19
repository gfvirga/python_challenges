import math

def getSmallestClockAngle(timeString, unit):
  hour, minute = [int(x) for x in timeString.split(":")]
  
  def getDegree(hour, minute):
    hour_ang = hour+(1/60*minute)
    if hour_ang >= 12:
      hour_ang = hour_ang - 12
    hour_loc = hour_ang*30
    minute_loc = minute*6
    angle  = int(abs(min((hour_loc - minute_loc),(minute_loc-hour_loc))))
    if angle > 180:
      return 360 - angle
    else:
      return angle
  
  if unit == "degrees":
    return getDegree(hour, minute)
  elif unit == "radians":
    return round(((math.pi*2)/360)*getDegree(hour, minute),4)


print(getSmallestClockAngle("03:00","radians"))