import time
import threading

def input_listener():
    global stop_requested
    while True:
        response = input()
        if response.lower() == "stop":
            stop_requested = True
            break

stop_requested = False

print("Type 'Start' to start the timer.")

while True:
    response = input()
    if response.lower() == "start":
        break

time.sleep(1)

print("Stopwatch started.")

counter = 0

thread = threading.Thread(target=input_listener)
thread.start()

while not stop_requested:
    time.sleep(1)
    hours = counter // 3600
    minutes = (counter % 3600) // 60
    seconds = counter % 60
    print(f"\rElapsed time: {hours:02d}:{minutes:02d}:{seconds:02d}", end="")
    counter += 1

print()
print("Stopwatch stopped.")
