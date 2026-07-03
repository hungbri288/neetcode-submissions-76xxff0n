from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.m = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        times = self.m[key]
        idx = times.bisect_right(timestamp) - 1
        if idx >= 0:
            closest = times.iloc[idx]
            return self.m[key][closest]
        return ""