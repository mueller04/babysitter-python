START_TIME_RATE = 12
BED_TIME = 22
BED_TIME_RATE = 8

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
        else:
            return None

    def totalPay(self, start_time, end_time):
        total = 0
        for count in range(start_time, end_time):
            if count < BED_TIME:
                total += START_TIME_RATE
            elif count >= BED_TIME:
                total+= BED_TIME_RATE
        return total
