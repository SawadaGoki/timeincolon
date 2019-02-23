__all__ = ["TimeInColon", "printResult"]

class TimeInColon:
    # format of "time" must be "[hours]:[minutes]"
    def __init__(self, time="00:00"):
        self.time = time

    # private method which converts time to "minutes" format
    def _convert_min(self, time: str):
        try:
            time_elements = time.split(":")
            h = int(time_elements[0])
            m = int(time_elements[1])
            return h * 60 + m
        except Exception as e:
            print(e)
            print('ERROR    Time format must be [hours]:[minutes]')

    # private method which returns "[hours]:[minutes]" format
    def _convert_origin(self, time_min: int):
        hours = str(time_min // 60)
        minutes = str(time_min % 60)
        # changing one digit into two digit
        if len(hours) == 1:
            hours = "0" + hours
        if len(minutes) == 1:
            minutes = "0" + minutes
        return hours + ":" + minutes

    def __add__(self, t2: str):
        t_in_min = self._convert_min(self.time)
        t2_in_min = self._convert_min(t2)
        sum_in_min = t_in_min + t2_in_min
        self.time = self._convert_origin(sum_in_min)
        return TimeInColon(self.time)
    
    def __sub__(self, t2: str):
        t_in_min = self._convert_min(self.time)
        t2_in_min = self._convert_min(t2)
        diff_in_min = t_in_min - t2_in_min
        self.time = self._convert_origin(diff_in_min)
        return TimeInColon(self.time)
    
    '''
    multipler and divisor number is not "00:00" format,
    but number(It can be string type)
    '''

    def __mul__(self, num: int):
        t_in_min = self._convert_min(self.time)
        prod_in_min = t_in_min * int(num)
        self.time = self._convert_origin(prod_in_min)
        return TimeInColon(self.time)

    def __truediv__(self, num: int):
        t_in_min = self._convert_min(self.time)
        quot_in_min = round(t_in_min / int(num))
        self.time = self._convert_origin(quot_in_min)
        return TimeInColon(self.time)

    # a public method which prints current result
    def printResult(self, instance_name=None):
        if instance_name:
            print("{0}: {1}".format(instance_name, self.time))
        else:
            print(self.time)

# a private method for testing
def _test():
    # "t = TimeInColon()" is the same as  "t = TimeInColon("00:00")"
    t = TimeInColon("10:02")
    t2 = TimeInColon("10:02")
    t3 = TimeInColon("00:03")
    t4 = TimeInColon("10:03")
    t + "10:01"
    t.printResult("t")
    t2 - "02:01"
    t2.printResult("t2")
    t3 * 2
    t3.printResult("t3")
    t4 / 3
    t4.printResult("t4")

if __name__ == "__main__":
    _test()

