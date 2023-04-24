# ============================= Instructor Comments =============================
# Overall: grade Submission
# Correctness: 60/60 pts
# Completeness: 25/25 pts
# Elegence: 15/15 pts
# Extra credit: 0/10 pts
# Total: 100/100 pts
# Grade: 
#
# ======================== Unit Testing Results (Complex) =======================
# Section-01: Method Validation Tests (Correct/Complete)
# Test-01: Valid Constructor Implementation (Queue/Stack/Node) - PASS
# Test-02: Valid Insert Implementation - PASS
# Test-03: Valid extractMax Implementation - PASS
# Test-04: Valid peekMax() Implementation - PASS
# Test-05: Valid isEmpty() Implementation - PASS
# Test-06: Valid isFull() Implementation - PASS
#
# Section-02: Proper Error Handeling Tests
# Error Test-01: Proper Constructor Error Handeling - PASS
# Error Test-02: Proper Insert Error Handeling - PASS
# Error Test-03: Proper ExtractMax Error Handeling - PASS
#
# Section-3 (Extra Credit): Sorted Array (heap_sort) - FAIL
#    ERROR: <PriorityQueue>.heapSort() ether crashed on valid input or returned false when it shouldn't.
#    returned: None
# ================================ End of Testing ===============================
# ===============================================================================


"""
Program: Project 2-Max Heap Priority Queue
Author:William Qiu
Date: 02/17/2023
Description: This is an implementation of Max Heap Priority Queue
Notes: For CS 313, Winter 2023, University of Oregon.

"""


# ============================== Exceptions =====================================
class PriorityQueueCapacityTypeError(Exception):
    """
    This exception gets raised when the queue is given the wrong type.
    """
    pass


class PriorityQueueCapacityBoundError(Exception):
    """
    This exception gets raised when the queue is given a negative or 0 value.
    """
    pass


class QueueIsFull(Exception):
    """
    This exception is raised when the queue is full.
    """
    pass


class QueueIsEmpty(Exception):
    """
    This exception is raised when the queue is empty.
    """
    pass


class InvalidInputTuple(Exception):
    """
    This exception gets raised when tuple input is invalid.
    """
    pass


class InputError(Exception):
    """
    This exception gets raised when the input is wrong.
    """
    pass


"""
<TODO> Add more exceptions if needed
"""


# ============================= PriorityQueue ===================================
class PriorityQueue():
    """
        Description:This is priority queue max heap implementation.
    """

    def __init__(self, capacity):
        """
            Description: This method is the constructor for the PQ class.
            Parameter: 1.capacity (needs to be an int greater than 0, otherwise raise exception).
        """
        self.capacity = capacity
        if type(capacity) != int:
            raise PriorityQueueCapacityTypeError(
                "Error:QueueCapacityTypeError. the Queue capacity is of the wrong type")
        if capacity <= 0:
            raise PriorityQueueCapacityBoundError("Error:QueueCapacityBoundError. The capacity is negative or 0 ")
        self._heap = []
        self.currentSize = 0

    def insert(self, item) -> bool:
        """
            Description: this is the insert function. it insert a given tuple(item) to the tree, by
                        adding a item to the end of the list and make swapping accrodingly.
            Parameter: 1. item: a tuple with 2 items, the first item is the key( positive int).
            returns: 1. True(when the insertion is successfully completed.
            Notes: Wrong input will raise exception
        """
        if self.isFull():
            raise QueueIsFull("Queue is full.")
        if type(item) != tuple:
            raise InvalidInputTuple("invalid tuple input")
        if len(item) != 2:
            raise InputError("invalid input: tuple length not 2(key and value)")
        if type(item[0]) != int:
            raise InputError("invalid input: tuple first item not key")
        if item[0] <= 0:
            raise InputError("invalid input: key must be greater than 0")

        i = len(self._heap)  # i= the size of the array = the next available index(because array start with 0)
        self._heap.append(item)  # set the last item in the array as the given item to insert
        self.currentSize += 1  # update the current size

        while (i > 0 and self._heap[self._getParent(i)][0] < self._heap[i][0]):  #
            temp = self._heap[self._getParent(i)]  # this is a swap function
            self._heap[self._getParent(i)] = item
            self._heap[i] = temp
            i = self._getParent(i)

        return True

    def extractMax(self) -> tuple:
        """
            Description: this method will give the tuple with max key and delete the original max while keep the tree in correct oder
            returns: the tuple with max key
        """
        if self.isEmpty():
            raise QueueIsEmpty("queue is empty")
        maxNode = self._heap[0]  # keep the value of the largest (0th item in the array)
        self._heap[0] = self._heap[len(self._heap) - 1]
        self._heap.pop()  # delete the last item
        self.currentSize -= 1  # update array size
        # print(self._heap)
        self._maxHeapify(0)
        return maxNode

    def peekMax(self) -> tuple:
        """
            Description:this method tells you the max tuple from the tree(but don't delete it)
            returns:1.tuple with max key in the tree
                    2.return false when the list is empty.
        """
        if self.isEmpty():
            return False
        else:
            return self._heap[0]

    def isEmpty(self) -> bool:
        """
            Description: This methods tell you if the heap is empty.
            returns: 1.True, if the heap is empty
                    2. False, if the heap is not empty.
        """
        if self.currentSize == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
            Description: This method tells if the heap is Full
            returns: 1.True, if the heap is full.
                    2. False, if the heap is not full.
        """
        if self.currentSize >= self.capacity:
            return True
        else:
            return False

    def build_max_heap(self, array):
        """
            Description: This method initialize the heap. take a given array and call maxheapfiy for every item
                        in the array to make an inorder maxheap.
            Parameter: an array.
        """
        self._heap = array
        self.currentSize = len(array)
        for i in range(self.currentSize // 2, -1, -1):
            self._maxHeapify(i)

    def heapSort(self, lst) -> list:
        """
            Description: take an unsorted array( in a heap sort way),and sort it from smallest to largest
            Parameter: 1. an array with valid inputs.
            returns:a sorted aray from smallest to largest
            Notes:
        """
        if type(lst) != list:
            raise InputError("invalid input:Wrong type")
        if len(lst) > self.capacity:
            raise InputError("invalid input: Wrong capacity")

        for i in range(0, len(lst), 1):
            if type([lst[i]]) != tuple:
                raise InputError("invalid input: not a list of tuples")
            if len(lst[i]) != 2:
                raise InputError("invalid input: tuple length not 2")
            if type(lst[i][0]) != int:
                raise InputError("invalid input: tuple first item not key")
            if lst[i][0] <= 0:
                raise InputError("invalid input: key must be greater than 0")

        self.build_max_heap(lst)
        for i in range(self.currentSize - 1, -1, -1):
            temp = self._heap[0]
            self._heap[0] = self._heap[self.currentSize]
            self._heap[self.currentSize] = temp
            self.currentSize -= 1
            self._maxHeapify(0)
        self.currentSize = len(self._heap)
        return self._heap

    def _maxHeapify(self, i):
        """
            Description: for index i, sort it to the correct order for a max heap
            Parameter:i, a index of any tuple
        """
        l = self._getLeftchild(i)
        r = self._getRightchild(i)
        if l < self.currentSize and self._heap[l][0] > self._heap[i][0]:
            largest = l
        else:
            largest = i
        if r < self.currentSize and self._heap[r][0] > self._heap[largest][0]:
            largest = r
        if largest != i:
            temp = self._heap[largest]
            self._heap[largest] = self._heap[i]
            self._heap[i] = temp
            self._maxHeapify(largest)

    def _getParent(self, i):
        """
            Description: get the key of the parent of a given tuple key
            Parameter: i, a key of a tuple
            returns:key of the parent.
        """
        return i // 2

    def _getLeftchild(self, i):
        """
            Description: get the key of the left child of a given tuple key
            Parameter:i, a key of a tuple
            returns: key of the left child
            Notes:
        """
        return 2 * i + 1

    def _getRightchild(self, i):
        """
            Description:get the key of the right child of a given tuple key
            Parameter:i, a key of a tuple
            returns:key of the right child.
            Notes:
        """
        return 2 * i + 2

    def __str__(self):
        """
            Description: magic method : str
            returns: a string presentation of the heap.
        """
        return f'{self._heap}'

# ===============================================================================
