class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> bool:
        if l > r:
            return False
        m = l + (r - l) // 2

        if nums[m] == target:
            return True
        if nums[m] < target:
            return self.binary_search(m+1, r, nums, target)
        return self.binary_search(l, m-1, nums, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            r = len(m) - 1
            if self.binary_search(0, r, m, target):
                return True
        return False
        

