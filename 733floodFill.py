from collections import deque
class Solution(object):
    def floodFill_bfs(self, image, sr, sc, newColor):
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor:
            q = deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                        q.append((x, y))
        return image

a = [[1,1,1],[1,1,0],[1,0,1]]
b = 1
c = 1
d = 2

print Solution().floodFill_bfs(a,b,c,d)