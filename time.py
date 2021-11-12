class time:
    listMonth = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    
    def __init__(self, month, day, hour, minute, second):
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second