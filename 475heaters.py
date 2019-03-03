class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        radius = 0
        for house in houses:
            left = 0
            right = len(heaters) - 1
            middle = (left + right) // 2

            while left < right - 1:
                middle = (left + right) // 2
                if house == heaters[middle]:
                    left = right = middle
                    break
                if house < heaters[middle]:
                    right = middle
                else:
                    left = middle

            if left == right:
                radius = max(radius, min(abs(house - heaters[left]), abs(house - heaters[middle])))
            else:
                radius = max(radius, min(abs(house - heaters[left]), abs(house - heaters[right])))

        return radius

    def findRadius1(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()

        maxDist = 0
        # for each house search for the nearest heater
        for h in houses:
            l,r = 0,len(heaters) - 1
            # stop when there are two candidates (instead of one)
            while r - l > 1:
                m = l+(r-l) // 2
                if heaters[m] < h:
                    # instead of l = m+1 in common binary search cases
                    l = m
                else:
                    r = m
            maxDist = max(maxDist,min(abs(heaters[l]-h),abs(heaters[r]-h)))
        return maxDist


    def findRadius2(self, houses, heaters):
        def closest_heater(x, h=heaters, i=0, j=len(heaters) - 1):
            if x < h[0]: return h[0]
            if h[-1] < x: return h[-1]
            while i <= j:
                mid = (i + j) // 2
                if x < h[mid]:
                    j = mid - 1
                elif h[mid] < x:
                    i = mid + 1
                else:
                    return h[mid]
            # now i == j + 1
            return h[i] if h[i] - x < x - h[j] else h[j]

        heaters.sort()
        return max(abs(house - closest_heater(house)) for house in houses)
if __name__ == "__main__":
    a,b = [1, 2, 3], [2]
    print Solution().findRadius2(a, b)