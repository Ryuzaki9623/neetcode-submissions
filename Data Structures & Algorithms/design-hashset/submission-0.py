class MyHashSet:

    def __init__(self):
        self._lst = []

    def add(self, key: int) -> None:
        if key not in self._lst:
            self._lst.append(key)

    def remove(self, key: int) -> None:
        if key in self._lst:
            self._lst.remove(key)

    def contains(self, key: int) -> bool:
        return key in self._lst


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)