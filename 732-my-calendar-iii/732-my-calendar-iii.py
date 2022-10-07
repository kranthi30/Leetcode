from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.events = SortedList()
        

    def book(self, start: int, end: int) -> int:
        L,R = 1,0
        self.events.add((start,L))
        self.events.add((end,R))
        res = 0
        cnt = 0
        for _,value in self.events:
            cnt += 1 if value == L else -1
            res = max(res,cnt)
        return res
            


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)