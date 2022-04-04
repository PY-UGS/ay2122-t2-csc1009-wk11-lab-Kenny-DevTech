class clockTime:
    def __init__(self) -> None:
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def setHours(self):
        self.hours=int(input("Set clock hours: "))
        while self.hours > 23 or self.hours < 0:
            print("Please enter hours between 0 to 23")
            self.hours=int(input("Set clock hours: "))

    def setMinutes(self):
        self.minutes=int(input("Set clock minutes: "))
        while self.minutes > 59 or self.minutes < 0:
            print("Please enter minutes between 0 to 59")
            self.minutes=int(input("Set clock minutes: "))

    def setSeconds(self):
        self.seconds=int(input("Set clock seconds: "))
        while self.seconds > 59 or self.seconds < 0:
            print("Please enter seconds between 0 to 59")
            self.seconds=int(input("Set clock seconds: "))
    
    def setTime(self):
        print("The clock time is based on 24-Hour")
        self.setHours()
        self.setMinutes()
        self.setSeconds()
    
    def showTime(self):
        print("\nThe time is: " + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))
        

newClock = clockTime()
newClock.setTime()
newClock.showTime()