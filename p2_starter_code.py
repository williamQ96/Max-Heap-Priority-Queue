"""
<TODO>
"""


# ============================== Exceptions =====================================
class QueueCapacityTypeError(Exception):
    """
    This exception gets raised when the queue is given the wrong type.
    """
    pass


class QueueCapacityBoundError(Exception):
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


"""
<TODO> Add more exceptions if needed
"""


# ============================= PriorityQueue ===================================
class PriorityQueue():
    """
    <TODO>
    """

# ===============================================================================
