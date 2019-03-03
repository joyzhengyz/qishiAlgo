class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        radius = 0
        for house in houses:
            l = 0
            r = len(heaters) - 1
            m = l + (r - l) // 2

            while l < r - 1:
                m = l + (r - l) // 2
                if house == heaters[m]:
                    l = r = m
                    break
                if house < heaters[m]:
                    r = m
                else:
                    l = m

            if l == r:
                radius = max(radius, min(abs(house - heaters[l]), abs(house - heaters[m])))
            else:
                radius = max(radius, min(abs(house - heaters[l]), abs(house - heaters[r])))

        return radius

if __name__ == "__main__":
    a,b = [1, 2, 3], [2]
    print Solution().findRadius(a, b)