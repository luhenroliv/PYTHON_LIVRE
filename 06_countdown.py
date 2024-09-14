import time

def start_timer():
    while True:
        try:
            t = int(input("Enter the time (in seconds): "))
            if t > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    input("Press Enter to start the timer...")

    while t > 0:
        minutes, seconds = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print()  
    print("Time is over!")
start_timer()
