class TimeMap:
    def __init__(self):
        # key is as normal
        # value will be tuple of (value, timestamp)
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []

        # assume timestamps stay ordered
        # if not we have to sort on timestamp every time we add
        #   (or use some sort of sorted list)
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        values = self.map[key]

        left = 0
        right = len(values)
        while left < right:
            mid = (left + right) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                left = mid + 1
            elif values[mid][1] > timestamp:
                right = mid

        return "" if right == 0 else values[right - 1][0]


def main():
    time_map = TimeMap()
    time_map.set(
        "foo", "bar", 1
    )  # store the key "foo" and value "bar" along with timestamp = 1.
    print(time_map.get("foo", 1))  # return "bar"
    print(
        time_map.get("foo", 3)
    )  # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    time_map.set(
        "foo", "bar2", 4
    )  # store the key "foo" and value "bar2" along with timestamp = 4.
    print(time_map.get("foo", 4))  # return "bar2"
    print(time_map.get("foo", 5))  # return "bar2"


main()
