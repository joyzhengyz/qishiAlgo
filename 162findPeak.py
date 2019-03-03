class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l


if __name__ == "__main__":
    a = [1,2,3,1]
    print Solution().findPeakElement(a)