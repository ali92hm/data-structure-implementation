import time


class Usage():
    def __init__(self, window: int, current_time: int):
        self.window_size = window
        self.start_time = current_time
        self.req_count = [0] * self.window_size

    def increment(self, current_time: int, n: int = 1):
        self.shift(current_time)
        self.req_count[current_time - self.start_time] += n

    def shift(self, current_time):
        start_new_window = current_time - self.window_size + 1
        end_old_window = self.start_time + self.window_size - 1

        # there is no overlap, full reset
        if start_new_window > end_old_window:
            self.start_time = current_time
            self.req_count = [0] * self.window_size
        # there is an over lap
        elif current_time > end_old_window:
            offset = current_time - end_old_window
            # the new startime is the old start time + offset
            self.start_time += offset

            # Shift elements by offset and set the rest to zero
            for i in range(self.window_size):
                if i + offset < self.window_size:
                    self.req_count[i] = self.req_count[i + offset]
                else:
                    self.req_count[i] = 0

    def get_total(self):
        return sum(self.req_count)


class RateLimiter():
    def __init__(self, max_req: int, time_window_sec: int):
        self._max_req = max_req
        self._time_window = time_window_sec
        self._usage = {}

    def is_req_allowed(self, user_id):
        current_time = int(time.time())

        # First time user
        if user_id not in self._usage:
            self._usage[user_id] = Usage(self._time_window, current_time)

        self._usage[user_id].shift(current_time)

        # If the total number of request with in window is less than max req
        if self._usage[user_id].get_total() < self._max_req:
            self._usage[user_id].increment(current_time)
            return True

        return False
