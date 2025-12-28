class AllOneHashMap:
    def __init__(self):
        self.cache = {}
        self.time_counter = 0
        self.set_all_value = None
        self.set_all_time = -1

    def set(self, key, value):
        self.time_counter += 1
        self.cache[key] = (value, self.time_counter)

    def get(self, key):
        if key not in self.cache:
            return -1
        value, timestamp = self.cache[key]
        if timestamp < self.set_all_time:
            return self.set_all_value
        return value

    def set_all(self, value):
        self.time_counter += 1
        self.set_all_value = value
        self.set_all_time = self.time_counter
