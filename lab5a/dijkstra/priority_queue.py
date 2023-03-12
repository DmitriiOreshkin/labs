from abc import ABC, abstractmethod


class IPriorityQueue(ABC):
    """ интерфейс приоритетной очереди """

    @abstractmethod
    def is_free(self) -> None:
        """проверка очереди на пустоту"""

    @abstractmethod
    def quantity(self) -> None:
        """получение числа элементов в очереди"""

    @abstractmethod
    def add(self, elem) -> None:
        """добавление элемента в очередь"""

    @abstractmethod
    def delete(self, elem) -> None:
        """удаление элемента из очереди"""

    @abstractmethod
    def max(self) -> None:
        """доступ к максимальному элементу очереди"""


class PriorityQueue(IPriorityQueue):
    """ реализация приоритетной очереди """

    def __init__(self, container=None) -> None:
        """ инициализация контейнера """
        self.container = []
        self.container_size = 0

        if container is not None:
            for elem in container:
                self.add(elem)

    def heapify(self, n, i) -> None:
        """ сортировка дерева """
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.container[i] < self.container[l]:
            largest = l

        if r < n and self.container[largest] < self.container[r]:
            largest = r

        if largest != i:
            self.container[i], self.container[largest] = self.container[largest], self.container[i]
            self.heapify(n, largest)

    def add(self, elem) -> None:
        """ добавление элемента,  """
        if self.container_size == 0:
            self.container.append(elem)
            self.container_size = len(self.container)
            return

        self.container.append(elem)
        self.container_size = len(self.container)
        for i in range((self.container_size // 2) - 1, -1, -1):
            self.heapify(self.container_size, i)

    def delete(self, elem):
        """ удаление элемента """
        for i in range(0, self.container_size):
            if elem == self.container[i]:
                break

        elem_index = len(self.container) - 1
        self.container[i], self.container[elem_index] = self.container[elem_index], self.container[i]

        elem = self.container.pop(elem_index)
        self.container_size = len(self.container)

        for i in range((len(self.container) // 2) - 1, -1, -1):
            self.heapify(self.container_size, i)

    def pop(self):
        """ удаление элемента """
        if len(self.container) >= 1:
            return self.container.pop(0)
        return None

    def max(self):
        """вывод максимального элемента"""
        if self.container_size == 0:
            return None
        return self.container[0]

    def quantity(self) -> int:
        """чисто элементов в очереди"""
        return self.container_size

    def is_free(self) -> bool:
        """пуста ли очередь"""
        return not self.container
