"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import *
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        intervals.sort(key=lambda x:x.start)
        min_heap=[]
        heappush(min_heap,intervals[0].end)
        for i in range(1,len(intervals)):
            if min_heap[0]<=intervals[i].start:
                heappop(min_heap)
            heappush(min_heap,intervals[i].end)
        return len(min_heap)
