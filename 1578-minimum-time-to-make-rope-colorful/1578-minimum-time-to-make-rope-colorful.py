class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost = 0
        max_cost = 0
        n = len(colors)
        for i in range(n):
            cost += neededTime[i]
            max_cost = max(max_cost,neededTime[i])
            if i == n-1 or colors[i] != colors[i+1]:
                cost -= max_cost
                max_cost = 0
        return cost
        