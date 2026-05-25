class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        current = self.map[key]
        for val in reversed(current):
            if val[1] <= timestamp:
                return val[0]
        
        return ""