class Solution(object):
    cache = set()

    def isMatch(self, s, p):
        p = self.preProcessPattern(p)
        return self.isMatchInternal(s, p)

    def preProcessPattern(self, p):
        res = ""
        c = ""
        i = 0
        while i < len(p):
            if c == "":
                res = res + p[i]

                if p[i] == "*":
                    c = p[i - 1: i + 1]

                i += 1
            elif i < len(p) - 1 and (c == p[i:i + 2] or c[0] == "." and p[i + 1] == "*"):
                i += 2
            else:
                c = ""

        return res

    def isMatchInternal(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True

        if len(p) == 0:
            return False

        if len(p) > 1 and p[1] == '*':

            if self.isMatch(s, p[2:]):
                return True

            for i in range(0, len(s)):
                if p[0] == '.' or p[0] == s[i]:

                    if self.isMatch(s[i + 1:], p[2:]):
                        return True

                else:
                    return False

            return False
        elif len(s) == 0:
            return False
        elif p[0] == s[0] or p[0] == '.':
            return self.isMatch(s[1:], p[1:])
        else:
            return False



s = Solution()


p = "a*a*a*a*a*a*a*a*a*a*c"

print s.preProcessPattern(p)
print s.isMatch("aaaaaaaaaaaaab",p)