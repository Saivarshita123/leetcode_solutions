import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()
        
        # Min-heap of available rooms
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        
        # Min-heap of (end_time, room_number)
        used_rooms = []
        
        # Count meetings per room
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Free rooms that have finished before current start time
            while used_rooms and used_rooms[0][0] <= start:
                end_time, room = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room)
            
            if available_rooms:
                # Assign to the lowest-numbered available room
                room = heapq.heappop(available_rooms)
                heapq.heappush(used_rooms, (end, room))
            else:
                # Delay the meeting
                end_time, room = heapq.heappop(used_rooms)
                new_end = end_time + duration
                heapq.heappush(used_rooms, (new_end, room))
            
            count[room] += 1
        
        # Return room with maximum meetings (smallest index if tie)
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
