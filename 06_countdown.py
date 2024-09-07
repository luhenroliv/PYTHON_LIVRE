import time

t = input("Enter the time (In seconds): ")

if t.isdigit():
    t = int(t)
else:
    print("Invalid input!")
    quit()

#120/60=2
#150/60=2|30

while t != 0: #0->False|1,2, ...->True
     minutes, seconds = divmod(t, 60)
     timer = "{:02d}:{:02d}".format(minutes, seconds)
     print(timer, end="\r")
     time.sleep(1)
     t = t - 1

#70/60->1|10->TIMER:"1:10"
#69/60->1|9->TIMER:"1:00"

print("Time is over!")