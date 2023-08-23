from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    sorted_intervals = sorted(intervals, key=lambda xx: xx[0])
    match sorted_intervals:
        case []:
            return []
        case [x]:
            return [x]
        case [to_merge, *rest]:
            result = []
            i = 1
            while i < len(sorted_intervals):
                current = sorted_intervals[i]
                if not to_merge:
                    to_merge = current
                elif current[0] > to_merge[1]:
                    result.append(to_merge)
                    to_merge = current
                else:
                    to_merge = [min(to_merge[0], current[0]),
                                max(to_merge[1], current[1])]
                i += 1
            if to_merge:
                result.append(to_merge)
            return result


def test_merge():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_merge1():
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
