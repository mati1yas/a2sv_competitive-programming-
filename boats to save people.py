class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ppl = people
        p1 = 0
        p2 = len(ppl)-1
        boat = 0
        
        while p1 <= p2 :
            if ppl[p1] + ppl[p2]> limit:
                boat+=1
                p2-=1
            else:
                p1+=1
                p2-=1
                boat+=1
        return boat 
