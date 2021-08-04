# https://leetcode.com/problems/min-cost-climbing-stairs

def minCostClimbingStairs(cost):
        memo = {}
        def rec(cost,index):
            if index >= len(cost)-2:
                return 0
            if index in memo:
                return memo[index]
            memo[index] = min(rec(cost,index+1)+cost[index+1],rec(cost,index+2) + cost[index+2])
            return memo[index]
        return rec(cost,-1)


print(minCostClimbingStairs([10,15,20]))
print(minCostClimbingStairs([10,15,5,89,1,9,3,29,1220]))