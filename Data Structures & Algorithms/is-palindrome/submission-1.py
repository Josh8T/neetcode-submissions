class Solution:
    def isPalindrome(self, s: str) -> bool:
        # check odd or even
        # if even then split into 2 groups and run 2 pointers from each end in the string
        # if odd then -1 then split into 2 group and run 2 pointers from each end

        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        if len(s) <= 1:
            return True
        

        print(s)
        start = 0
        end = len(s)-1
        if len(s) % 2 != 0:
            mid = len(s)//2 + 1
            for i in range(len(s)):
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                    if mid == start:
                        return True
                else:
                    return False
            return True
        else:
            for i in range(len(s)):
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True

                
                