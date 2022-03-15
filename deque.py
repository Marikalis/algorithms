# ID 64827726
class Deque:
    def __init__(self, max_size):
        self._data = [None] * max_size
        self._front = - 1
        self._back = 0
        self._size = 0

    def push_back(self, value):
        self._back = self._push(self._back, 1, value)

    def pop_back(self):
        self._back, value = self._pop(self._back, 1)
        return value

    def push_front(self, value):
        self._front = self._push(self._front, -1, value)

    def pop_front(self):
        self._front, value = self._pop(self._front, -1)
        return value

    def _push(self, index, index_change, value):
        if self._size >= len(self._data):
            raise IndexError('Достигнуто максимальное количество элементов в буфере.')
        self._data[index] = value
        self._size += 1
        return (index + index_change) % len(self._data)

    def _pop(self, index, index_change):
        if self._size <= 0:
            raise IndexError('Буфер пуст.')
        new_index = (index - index_change) % len(self._data)
        self._size -= 1
        return new_index, self._data[new_index]



if __name__ == '__main__':
    count_command = int(input())
    queue = Deque(int(input()))
    for _ in range(count_command):
        verb, *values = input().split()
        try:
            result = getattr(queue, verb)(*values)
        except(IndexError):
            result = 'error'
        except AttributeError:
            raise ValueError(
                f'Команда не поддерживается: "{count_command}".')
        if result is not None:
            print(result)
