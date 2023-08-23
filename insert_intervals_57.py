from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    to_merge = newInterval
    if not intervals:
        result.append(to_merge)
        to_merge = None

    for interval in intervals:
        if to_merge is None:
            result.append(interval)
        elif to_merge[1] < interval[0]:
            result.append(to_merge)
            result.append(interval)
            to_merge = None
        elif to_merge[0] > interval[1]:
            result.append(interval)
        else:
            to_merge = [min(interval[0], to_merge[0]), max(interval[1], to_merge[1])]
    if to_merge:
        result.append(to_merge)
    return result


def test_insert():
    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]
    assert insert(intervals, new_interval) == [[1, 5], [6, 9]]


def test_insert_2():
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_interval = [4, 8]
    assert insert(intervals, new_interval) == [[1, 2], [3, 10], [12, 16]]


def test_insert_3():
    assert insert([], [5, 7]) == [[5, 7]]


def test_insert_4():
    assert insert([[1, 5]], [2, 3]) == [[1, 5]]


def test_insert_5():
    assert insert([[2, 5], [6, 7], [8, 9]], [0, 1]) == [[0, 1], [2, 5], [6, 7], [8, 9]]
