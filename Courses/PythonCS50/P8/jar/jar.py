class Jar:
    def __init__(self, capacity=12):
        # is instance checks if the given value is a type of something sent as param, eg is capacity a int
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Negative not allowed")
        # underscore determines that the varaible is the actual variable holding the values and not a proprotey
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        # updates the actual value using underscore
        if self._size + n > self.capacity:
            raise ValueError("Too many cookies")
        else:
            self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    

jar = Jar(10)
# testing
print(jar.size)
jar.deposit(5)
print(jar.size)
jar.withdraw(3)
print(jar.size)

