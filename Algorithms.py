class MergeSort:
    @staticmethod
    def sort(items):
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left = MergeSort.sort(items[:mid])
        right = MergeSort.sort(items[mid:])

        return MergeSort.merge(left, right)

    @staticmethod
    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged.extend(left[left_index:])
        merged.extend(right[right_index:])
        return merged

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def put(self, item):
        self.queue.append(item)
        self.queue = MergeSort.sort(self.queue)

    def get(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0] if self.queue else None

    def __len__(self):
        return len(self.queue)
