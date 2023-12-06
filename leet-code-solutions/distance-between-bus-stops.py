class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
  
        total_distance = sum(distance)
        
        if start > destination:
            start, destination = destination, start
        
        distance1 = sum(distance[start:destination])
        
        distance2 = total_distance - distance1
        
        return min(distance1, distance2)

