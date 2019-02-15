import time

class CurrentWeek(object):
    def __init__(self):
        pass

    def currentWeek(self):
        week = time.strftime("%A", time.localtime())
        if 'Sunday' == week:
            return '星期天'
        elif 'Monday' == week:
            return '星期一'
        elif 'Tuesday' == week:
            return '星期二'
        elif 'Wednesday' == week:
            return '星期三'
        elif 'Thursday' == week:
            return '星期四'
        elif 'Friday' == week:
            return '星期五'
        elif 'Saturday' == week:
            return '星期六'



