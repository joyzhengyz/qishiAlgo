import math
class Solution(object):
    def minmaxGasDist(self,stations, k):
        """
        :type stations: List[int]
        :type k: int
        :rtype: float
        """
        #0.000001 == 1e-6
        left, right = 1e-6, stations[-1] - stations[0]

        while left + 1e-6 < right:
            mid = left + (right - left) / 2
            count = 0
            print "zip(stations, stations[1:])", zip(stations, stations[1:])
            for a, b in zip(stations, stations[1:]):
                count += math.ceil((b - a) / mid) - 1
                print a, b, count, math.ceil((b - a) / mid)
            if count > k:
                left = mid
            else:
                right = mid
        return right

if __name__ == "__main__":
    stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 9
    print Solution().minmaxGasDist(stations,k)