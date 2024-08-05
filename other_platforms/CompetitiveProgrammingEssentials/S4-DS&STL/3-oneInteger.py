#You are given a list of integers nums. You can reduce the length of nums by taking any two integers, removing them, and appending their sum to the end. The cost of doing this is the sum of the two integers you removed.
#Return the minimum total cost of reducing nums to one integer.
#https://www.geeksforgeeks.org/minimize-the-sum-calculated-by-repeatedly-removing-any-two-elements-and-inserting-their-sum-to-the-array/
#https://www.udemy.com/course/competitive-programming-algorithms-coding-minutes/learn/quiz/5251594#questions
import heapq
def solve(nums):
    heapq.heapify(nums)
    sum=0
    while len(nums)>1:
        a,b=heapq.heappop(nums),heapq.heappop(nums)
        sum+=(a+b)
        heapq.heappush(nums,a+b)
    return sum

print(solve([1, 2, 3, 4, 5])) # 33
print(solve([1, 4,7,10])) # 39
print(solve([1, 3,7, 5,6])) # 48