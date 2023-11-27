import math

seconds = int(input("Enter seconds: "))

hours = math.floor(seconds%(24*3600)/3600)
secondss = seconds%60

seconds %= 3600
minutes = math.floor(seconds/60)

print(f"""
      hours: {hours}
      minutes: {minutes}
      seconds: {secondss}
      """
      )

