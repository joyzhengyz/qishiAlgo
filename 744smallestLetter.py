class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1]:
            return letters[0]
        l, r = 0, len(letters) - 1
        while l < r:
            m = l + (r-l) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1
        return letters[l]

if __name__ == "__main__":
    # letters = ["c", "f", "j"]
    # target = "a"

    # letters = ["c", "f", "j"]
    # target = "c"

    # letters = ["c", "f", "j"]
    # target = "d"

    # letters = ["c", "f", "j"]
    # target = "g"

    # letters = ["c", "f", "j"]
    # target = "j"

    letters = ["c", "f", "j"]
    target = "k"

    print Solution().nextGreatestLetter(letters,target)