"""
Author: Jared Hall, <your_name_here>
Last Modified Date: 01/28/2022
Description: This file contains some useful methods to help you test your code.
             Also contains some starter codes for testing.
"""

from p2_live_code import *
import pytest


def heapValidator(heap):
    """
    Description: This method validates the heap.
    Usage:  heapValidator(PQ._heap)
    Returns: tuple. (bool, str)
    Format: (True/False, reason)
    """

    returnValue = (True, "PASSED")
    # Step-01: Varifies that the heap contains tuples of the correct format.
    if (type(heap) != list):
        returnValue = (False, "FAILED: heap must be a list.")
    elif (len(heap) == 0):
        pass
    else:
        start = 1 if (type(heap[0]) != tuple) else 0
        for i in range(start, len(heap), 1):
            if (type(heap[i]) != tuple):
                returnValue = (False, "FAILED: Heap must consist of tuples")
            elif (type(heap[i][0]) != int or heap[i][0] <= 0):
                returnValue = (False, "FAILED: each tuple in the heap must " + \
                               "have a positive int as the priority")
            else:
                try:
                    heap[i][1]
                except:
                    returnValue = (False, "FAILED: Incorrectly formatted " + \
                                   "tuple. Must have an item to queue")

    # step-02: Validate the heap. (e.g., make sure all nodes obey heap rules)
    if (returnValue[0] and len(heap) != 0):
        start = 1 if (type(heap[0]) != tuple) else 0
        if (len(heap) > start):
            parentIndex = 0
            for i in range(start, len(heap), 1):
                if (i == 0):
                    parentIndex = 0
                else:
                    parentIndex = (i - 2) // 2 if (i % 2 == 0) else (i - 1) // 2
                if (heap[i][0] > heap[parentIndex][0]):
                    returnValue = (False, f"Invalid heap detected: Child-{i}" + \
                                   f" {heap[i]} > parent-{parentIndex} {heap[parentIndex]}")
                    break

    return returnValue


class TestMain:

    def test_initValid(self):
        # Hint: test a valid constructor call
        PQ = PriorityQueue(10)
        self.start = 1 if (len(PQ._heap) == 1) else 0

        assert PQ.currentSize == 0
        assert PQ.capacity == 10
        assert type(PQ._heap) == list
        assert len(PQ._heap) < 2

    def test_initInvalidNonInt(self):
        # Hint: Test the constructor with something that is not an int
        with pytest.raises(PriorityQueueCapacityTypeError):
            PQ = PriorityQueue("Hi")

    def test_initInvalidNeg(self):
        # Hint: Test the constructor with a negative int
        with pytest.raises(PriorityQueueCapacityBoundError):
            PQ = PriorityQueue(-1)

        with pytest.raises(PriorityQueueCapacityBoundError):
            PQ = PriorityQueue(0)

    def test_strValid(self):
        # Hint: Test the string method See format from project document.
        PQ = PriorityQueue(10)
        val = "VAL"
        heap = [(20, val), (15, val), (10, val), (11, val), (14, val), (5, val), (8, val)]
        control = str(heap)
        PQ._heap = heap

        result = PQ.__str__()

        assert result == control

    def test_insertInvalidInput(self):
        # Hint: Test what happens when you try to insert invalid input.
        PQ = PriorityQueue(10)
        err1 = "hi"
        err2 = ("s", "a")
        err3 = (3)
        err4 = (None)

        with pytest.raises(InvalidInputTuple):
            PQ.insert(err1)

        with pytest.raises(InvalidInputTuple):
            PQ.insert(err2)

        with pytest.raises(InvalidInputTuple):
            PQ.insert(err3)

        with pytest.raises(InvalidInputTuple):
            PQ.insert(err4)

        assert err1 not in PQ._heap
        assert err2 not in PQ._heap
        assert err3 not in PQ._heap
        assert err4 not in PQ._heap

    def test_insertFull(self):
        # Hint: Test what happens if you try to insert into a full PQ
        PQ = PriorityQueue(7)
        val = "a"
        heap = [(20, val), (15, val), (10, val), (11, val), (14, val), (5, val), (8, val)]
        PQ._heap = heap
        PQ.currentSize = 7

        with pytest.raises(QueueIsFull):
            PQ.insert((25, val))

    def test_insertValid(self):
        # Hint: Test what happens when you try to insert valid input.
        #      Dont forget to validate the heap! (^,^)
        PQ = PriorityQueue(10)
        val = "a"
        heap = [(20, val), (15, val), (10, val), (11, val), (14, val), (5, val), (8, val)]
        PQ._heap = heap
        PQ.currentSize = 7

        T1 = (18, val)
        result = PQ.insert(T1)

        assert result == True
        assert T1 in PQ._heap

    def test_extractMaxEmpty(self):
        # Hint: Test what happens if you try to extract when the PQ is empty
        pass

    def test_extractMaxNotEmpty(self):
        # Hint: Test what happens if you try to extract when the PQ is not empty
        pass

    def test_peekMaxEmpty(self):
        # Hint: Test what happens if you try to peek when the PQ is empty
        pass

    def test_peekMaxNotEmpty(self):
        # Hint: Test what happens if you try to peek when the PQ is not empty
        pass

    def test_isEmptyNoItems(self):
        # Hint: Test what happens when isEmpty is called when the PQ is empty.
        pass

    def test_isEmptyNotEmpty(self):
        # test what happens if isEmpty is called when the queue is not empty.
        pass

    def test_isFullNoItems(self):
        # Hint: Test what happens when isFull is called when the PQ is empty.
        pass

    def test_isFullFull(self):
        # test what happens if isFull is called when the queue is full.
        pass


"""
<TODO> More test is needed. Add as many as you needed.
"""
