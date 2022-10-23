from threading import Timer


class RepeatTimer(Timer):
    """ run timer forever (until cancel)"""

    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
