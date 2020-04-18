import time

class Clock:
    def __init__(self, iHours, iMinutes, iSeconds, iAMPM):
        self.__hours = iHours
        self.__minutes = iMinutes
        self.__seconds = iSeconds
        self.__ampm = iAMPM

    def print_time(self):
        time = ''

        if self.__hours < 10:
            time += "0"
        time += str(self.__hours)

        time += ":"

        if self.__minutes < 10:
            time += "0"
        time += str(self.__minutes)

        time += ":"

        if self.__seconds < 10:
            time += "0"
        time += str(self.__seconds)

        time += " "
        time += self.__ampm

        print(time)

    def tick(self):
        self.__seconds += 1

        if self.__seconds == 60:
            self.__minutes += 1
            self.__seconds = 0
        if self.__minutes == 60:
            self.__hours += 1
            self.__minutes = 0
        if self.__hours == 12 and self.__minutes == 0 and self.__seconds == 0:
            if self.__ampm == "AM":
                self.__ampm = "PM"
            else:
                self.__ampm = "AM"
        self.ring_alarm()

    def set_alarm(self, aHours, aMinutes, aSeconds, aAMPM):
        self.__alarmHours = aHours
        self.__alarmMinutes = aMinutes
        self.__alarmSeconds = aSeconds
        self.__alarmAMPM = aAMPM

    def ring_alarm(self):
        if self.__hours == self.__alarmHours and self.__minutes == self.__alarmMinutes and self.__seconds == self.__alarmSeconds and self.__ampm == self.__alarmAMPM:
            print("BEEP BEEP BEEP")

def main():
    myClock = Clock(12, 0, 0, "AM")
    myClock.set_alarm(12, 0, 10, "AM")

    while (True):
        myClock.tick()
        myClock.print_time()
        time.sleep(1)

main()

