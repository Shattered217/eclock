import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time's up!")

def focus_timer():
    print("Welcome to Focus Timer!\n")
    print("Please enter the duration of your work session (in minutes):")
    work_duration = int(input())
    print("Please enter the duration of your break (in minutes):")
    break_duration = int(input())
    print("\nStarting your work session now!\n")
    while True:
        countdown(work_duration * 60)
        print("Time for a break!")
        countdown(break_duration * 60)
        print("Back to work!\n")
