import time

seconds = int(input("enter the time here in seconds"))

def countdownTimer (seconds):
    while seconds :
      mins = int(seconds / 60)
      scs = int(seconds % 60)
      timer = f"{mins} : {scs}"
      time.sleep(1)
      seconds -= 1
      print(timer,end = '\r')
    print("timeout")
countdownTimer(seconds)
