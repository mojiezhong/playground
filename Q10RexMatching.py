class Solution(object):
    def isMatch(self, s, p):
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
