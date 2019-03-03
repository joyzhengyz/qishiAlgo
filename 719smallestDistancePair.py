class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        print(nums, r)
        while l <= r:
            mid = l + (r-l) // 2
            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and abs(nums[j] - nums[i]) <= mid:
                    j += 1
                count += (j - i - 1)
            if count < k:
                l = mid + 1
            else:
                r = mid - 1
        return l

if __name__ == "__main__":
    nums = [1,3,9]
    k = 1
    print Solution().smallestDistancePair(nums, k)