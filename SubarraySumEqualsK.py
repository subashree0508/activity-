class Solution:
    def subarraySum(self, nums, k):
        count = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
        return count
