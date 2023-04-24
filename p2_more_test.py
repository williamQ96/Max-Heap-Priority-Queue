"""
Author: Jared Hall, <your_name_here>
Last Modified Date: 01/28/2022
Description: This file contains some useful methods to help you test your code.
             Also contains some starter codes for testing.
"""
from p2_live_code import *
import pytest


def toSTR(heap, start):
    root = heap[start]
    N1 = heap[1 + start]
    N2 = heap[2 + start]
    N3 = heap[3 + start]
    N4 = heap[4 + start]
    N5 = heap[5 + start]
    N6 = heap[6 + start] if ((6 + start) < len(heap)) else ""
    Rep = f"#                       {root}                        \n"
    Rep += f"#         {N1}                 {N2}         \n"
    Rep += f"#  {N3}  {N4}   {N5}  {N6}  \n"
    return Rep


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
    # print("\n====================================================================\n")
    # print(f"Current heap: {heap}\n")
    if (returnValue[0] and len(heap) != 0):
        start = 1 if (type(heap[0]) != tuple) else 0
        # print(f"Starting position: {start}\n")
        # print("Heap representation: \n", toSTR(heap, start))
        if (len(heap) > start):
            parentIndex = start
            for i in range(start, len(heap), 1):
                if (i == start):
                    parentIndex = start
                else:
                    if (start == 0):
                        parentIndex = ((i - 2) // 2) if (i % 2 == 0) else ((i - 1) // 2)
                    else:
                        parentIndex = ((i) // 2) if (i % 2 == 0) else ((i - 1) // 2)
                if (heap[i][0] > heap[parentIndex][0]):
                    returnValue = (False, f"Invalid heap detected: Child-{i}" + \
                                   f" {heap[i]} > parent-{parentIndex} {heap[parentIndex]}")
                    break
    # print("\n====================================================================\n")

    return returnValue


class TestMain():

    def test_initValid(self):
        # Hint: test a valid constructor call
        pq = PriorityQueue(20)
        assert pq.currentSize == 0
        assert pq.capacity == 20
        try:
            pq._heap
        except:
            raise Exception

    def test_initInvalidNonInt(self):
        # Hint: Test the constructor with something that is not an int
        with pytest.raises(PriorityQueueCapacityTypeError):
            pq = PriorityQueue("5")

    def test_initInvalidNeg(self):
        # Hint: Test the constructor with a negative int
        with pytest.raises(PriorityQueueCapacityBoundError):
            pq = PriorityQueue(-5)

    def test_insertInvalidInput(self):
        # Hint: Test what happens when you try to insert invalid input.
        PQ = PriorityQueue(10)
        with pytest.raises(InvalidInputTuple):
            PQ.insert(1)

    def test_insertFull(self):
        # Hint: Test what happens if you try to insert into a full PQ
        pq = PriorityQueue(7)
        val = "a"
        heap = [(20, val), (15, val), (10, val), (11, val), (14, val), (5, val), (8, val)]
        pq.currentSize = 7
        pq._heap = heap
        with pytest.raises(QueueIsFull):
            pq.insert((6, "6"))

    def test_insertValid(self):
        # Hint: Test what happens when you try to insert valid input.
        #      Dont forget to validate the heap! (^,^)
        pq = PriorityQueue(10)
        val = "a"
        heap = [(20, val), (15, val), (10, val), (11, val), (14, val), (5, val), (8, val)]
        pq.currentSize = 7
        pq._heap = heap
        T1 = (18, "a")
        ret = pq.insert(T1)

        assert ret == True
        assert T1 in pq._heap
        assert pq.currentSize == 8
        ret = heapValidator(pq._heap)
        assert ret[0], ret[1] + toSTR(pq._heap, 0)

    def test_extractMaxEmpty(self):
        # Hint: Test what happens if you try to extract when the PQ is empty
        pq = PriorityQueue(10)
        with pytest.raises(QueueIsEmpty):
            pq.extractMax()

    def test_extractMaxNotEmpty(self):
        # Hint: Test what happens if you try to extract when the PQ is not empty
        pq = PriorityQueue(10)
        val = "a"
        heap = [(20, val), (15, val), (10, val), (11, val), (14, val), (5, val), (8, val)]
        pq.currentSize = 7
        pq._heap = heap
        ret = pq.extractMax()
        T1 = (20, val)
        assert ret == T1
        assert T1 not in pq._heap
        assert pq.currentSize == 6
        ret = heapValidator(pq._heap)
        assert ret[0], ret[1] + toSTR(pq._heap, 0)

    def test_peekMaxEmpty(self):
        # Hint: Test what happens if you try to peek when the PQ is empty
        pq = PriorityQueue(10)
        ret = pq.peekMax()
        assert ret == False

    def test_peekMaxNotEmpty(self):
        # Hint: Test what happens if you try to peek when the PQ is not empty
        pq = PriorityQueue(10)
        val = "a"
        heap = [(20, val), (15, val), (10, val), (11, val), (14, val), (5, val), (8, val)]
        pq.currentSize = 7
        pq._heap = heap

        ret = pq.peekMax()
        T1 = (20, val)
        assert T1 == ret
        assert pq.currentSize == 7
        assert T1 == pq._heap[0]
