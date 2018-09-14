# Provides a class of stopwatch objects.
import time

'''
Stopwatch object. Measures the duration between a .tic() call
and a .toc() call in units of seconds.'''
class Timer(object):
    # Constructor. Initializes startTime to
    # the time of construction.
    def __init__(self):
        self.startTime = time.time()

    # Resets the timer.
    def tic(self):
        self.startTime = time.time()

    # Returns time elapsed (in seconds) since the last
    # .tic() was called.
    def toc(self):
        return time.time() - self.startTime

# Object used for the tic() and toc() functions that can
# be used in the global scope.
masterTimer = Timer()

# Resets the master timer
def tic():
    masterTimer.tic()

# Returns seconds elapsed since last tic() was called.
def toc():
    return masterTimer.toc()