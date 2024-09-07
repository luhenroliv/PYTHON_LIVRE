import time

# Print the initial message
print("Type 'Start' to start the timer.")

# Infinite loop to wait for the "Start" command
while True:
    response = input()
    if response.lower() == "start":
        break

# Pause for 1 second to refresh the screen
time.sleep(1)

# Prints the stopwatch start message
print("Stopwatch started.")

# Initialize the counter
counter = 0

# Infinite loop for stopwatch counting
while True:
    # Wait a second
    time.sleep(1)
    # Calculates elapsed time in hours, minutes and seconds
    hours = counter // 3600
    minutes = (counter % 3600) // 60
    seconds = counter % 60
    # Prints elapsed time in time format
    print(f"\rElapsed time: {hours:02d}:{minutes:02d}:{seconds:02d}", end="")
    # increments the counter
    counter += 1