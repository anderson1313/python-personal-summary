class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=len(nums)
        dp=[0 for i in range(l)]
        dp[0]=nums[0]
        maxnum=dp[0]
        for i in range(1,l):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            if dp[i]>maxnum:
                maxnum=dp[i]
        return maxnum