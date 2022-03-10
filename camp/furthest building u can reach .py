class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        arr = []

        for i in range(len(heights)-1):
            h=heights[i+1]-heights[i]
            if h<=0:
                continue
            heappush(arr,h)
            if len(arr)>ladders:
                min_height_dif=heappop(arr)
                bricks-=min_height_dif
            if bricks<0:
                return i 
        return len(heights)-1
