class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        current = self.map[key]

        left, right = 0, len(current)-1

        latest = float("-inf")
        result = None
        while left <= right:
            mid = left + (right - left) // 2

            if current[mid][1] == timestamp:
                return current[mid][0]
            elif current[mid][1] > timestamp:
                right = mid - 1
            else:
                if latest < current[mid][1]:
                    latest = current[mid][1]
                    result = current[mid][0]
                left = mid + 1
                

        if result:
            return result
        return ""