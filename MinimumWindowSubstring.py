class Solution:
    def minWindow(self, s, t):
        result = ""
        for i in range(len(s)):
            temp = ""
            for j in range(i, len(s)):
                temp += s[j]
                ok = True
                for ch in t:
                    if temp.count(ch) < t.count(ch):
                        ok = False
                        break
                if ok:
                    if result == "" or len(temp) < len(result):
                        result = temp
                    break
        return result
