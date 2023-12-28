class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            sum += i
            if sum == target:
                return True
        return False

s = Solution()
nums = [2,7,11,15]
target = 9
result = s.twoSum(nums,target)
print(result)