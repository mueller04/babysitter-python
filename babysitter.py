class Babysitter():

    def calculate(self, start_time):
        isValidTime = self.validateTime(start_time)
        if isValidTime == None:
            return 60;
        else:
            return isValidTime

    def validateTime(self, start_time):
        if start_time < 17 and start_time > 3:
            return "start time cannot be before 5pm or after 3am"
        else:
            return None
