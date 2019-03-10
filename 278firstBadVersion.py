def firstBadVersion(n):
    l = 0
    r = n
    while l<r:
        m = l + (r-l)/2
        if not isBadVersion(m):
            l = m + 1
        else:
            r = m

    return l