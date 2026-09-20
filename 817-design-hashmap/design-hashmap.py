class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data[i] = (key, value)  
                return
        self.data.append((key, value))  

    def get(self, key: int) -> int:
        for pair in self.data:
            if pair[0] == key:
                return pair[1]
        return -1  # not found

    def remove(self, key: int) -> None:
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data.pop(i)
                return
