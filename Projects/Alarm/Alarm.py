import time
import winsound  # This modual Only work in windows

print("Made by 007")


def my_alarm():
    try:
        my_time = list(map(int, input("Enter time in H, M, S\n").split()))
        if len(mytime) == 3:
            total_seconds = my_time[0] * 60 * 60 + my_time[1] * 60 + my_time[2]
            time.sleep(total_seconds)
            frequency = 2500  # set frequency to 2500 Hertz
            duration = 1000  # set Duration to 1000 ms == 1 second
            winsound.Beep(frequency, duration)
        else:
            print("Please enter time in corret format hours, mint, second\n")
            my_alarm()
    except Exception as e:
        print("This is the exception\n", e, "So!, Please enter correct details")
        my_alarm()


my_alarm()
