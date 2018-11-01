# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        rList = []
        res = 0
        for char in s:
            if char in rList:
                res = max(res, len(rList))
                rList = rList[rList.index(char)+1:len(rList)]
            rList.append(char)
        return max(res, len(rList))