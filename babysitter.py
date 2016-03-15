START_TIME_RATE = 12
BED_TIME = 22
BED_TIME_RATE = 8
MIDNIGHT = 24
MIDNIGHT_RATE = 16

class Babysitter():

    def calculate(self, start_time, end_time):
        isValidTime = self.validateTime(start_time, end_time)
        if isValidTime == None:
            return self.totalPay(start_time, end_time)
        else:
            return isValidTime

    def validateTime(self, start_time, end_time):
        if start_time < 17 and start_time > 3:
            return "start time cannot be before 5pm or after 3am"
        elif end_time > 4 and end_time < 18:
            return "end time cannot be before 6pm or after 4am"
        else:
            return None

    def totalPay(self, start_time, end_time):
        if end_time < 5:
            end_time += 24

        print "start_time"
        print start_time
        print end_time
        print "next"

        total = 0
        for count in range(start_time, end_time):
            if count < BED_TIME:
                total += START_TIME_RATE
            elif count >= BED_TIME and count < MIDNIGHT:
                total += BED_TIME_RATE
            elif count >= MIDNIGHT:
                total += MIDNIGHT_RATE
        return total
