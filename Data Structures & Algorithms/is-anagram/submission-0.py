class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort algo nlogn
        # 2 nlogn because 2 list
        # compare 2 list sorted
        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))

        if s_sorted == t_sorted:
            return True
        else:
            return False