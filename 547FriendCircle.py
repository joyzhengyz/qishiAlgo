try:
    import queue
except ImportError:
    import Queue as queue
def findCircleNum(M):
    fc = 0
    q = queue.Queue()
    for row in range(len(M)):
        for col in range(len(M[0])):
            if M[row][col] == 1:
                fc += 1
                q.put((row, col))
                while not q.empty():
                    a = q.get()
                    M[a[0]][a[1]] = 0
                    M[a[1]][a[0]] = 0
                    for i in range(len(M[0])):
                        if M[a[1]][i] == 1:
                            q.put((a[1], i))
    return fc

a = [[1,1,0],[1,1,0],[0,0,1]]

print findCircleNum(a)