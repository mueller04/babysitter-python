START_TIME_RATE = 12

class Babysitter():

    def calculate(self, start_time, end_time):
        isValidTime = self.validateTime(start_time, end_time)
        if isValidTime == None:
            return START_TIME_RATE * (end_time - start_time);
        else:
            return isValidTime

    def validateTime(self, start_time, end_time):
        if start_time < 17 and start_time > 3:
            return "start time cannot be before 5pm or after 3am"
        else:
            return None
