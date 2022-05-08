class Heap:
    """
     Heap Data Structure Max-Heap
     Top element will be always maximum element
     Followed by left and right.
    """

    def __init__(self):
        self.arr = []
        self.size = -1

    def insert_element(self, data):
        self.size += 1
        self.arr.append(data)

        Heap.build_heap(self.arr)


    def delete_element(self, pos):
        if self.size < 0 or pos > self.size:
            return -1

        self.size -= 1
        self.arr[pos] = -1

        Heap.heapify(self.arr, len(self.arr) - 1, pos)

    @staticmethod
    def heapify(arr, n, current_large):
        largest = current_large
        left = int(current_large * 2 + 1)
        right = int(current_large * 2 + 2)

        if left <= n and arr[left] > arr[largest]:
            largest = left

        if right <= n and arr[right] > arr[largest]:
            largest = right

        if largest != current_large:
            arr[largest] = arr[largest] ^ arr[current_large]
            arr[current_large] = arr[largest] ^ arr[current_large]
            arr[largest] = arr[largest] ^ arr[current_large]

            Heap.heapify(arr, n, largest)

    @staticmethod
    def build_heap(arr):
        half = int(len(arr) / 2)
        while half >= 0:
            Heap.heapify(arr, len(arr) - 1, half)
            half -= 1
