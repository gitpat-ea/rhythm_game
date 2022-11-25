import time as time

class NumVariables:
    """Class of numeric variables"""
    def __init__(self, num = 0):
        self._num = num

    def adder(self, arg):
        self._num += arg

    def setter(self, arg):
        self._num = arg

    def timer_setter(self):         # Sets value to current time
        self._num = time.time()

    def getter(self):
        return self._num

class BullVariables:
    """Class of Bullian variables"""
    def __init__(self, init_bul = True):
        self._bul = init_bul

    def setter(self, arg):
        self._bul = arg

    def timer(self):            # Returns True or False depending on current time
        if ((time.time() - start_time.getter())%1 <= 0.1) or ((time.time() - start_time.getter())%1 >= 0.9):
            self._bul = True
        else:
            self._bul = False

    def changer(self):
        if self._bul:
            self._bul = False
        else:
            self._bul = True

    def getter(self):
        return self._bul


start_time = NumVariables()
TimerBull = BullVariables()