class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return [max(nums)]
        
        output = []
        q = deque()

        for i in range(len(nums)):
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # Maintain decreasing order in deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)
            
            # Once we have hit at least size k, append to output
            if i >= k - 1:
                output.append(nums[q[0]])
        
        return output
