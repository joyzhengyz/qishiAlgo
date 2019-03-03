class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            print "l, r, mid ", l, r, mid
            if nums[m] > nums[m + 1] and nums[m] > nums[m - 1]:
                return m
            elif nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m
        return l


if __name__ == "__main__":
    a = [1,2,3,1]
    # a = [1,9,4,4,4,2,1]
    print Solution().findPeakElement(a)