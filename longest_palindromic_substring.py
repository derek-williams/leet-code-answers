#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

class Solution:
    def longestPalindrome(self, s):
        '''
        :type s: str
        :rtype: str
        '''
        if len(s)<=1: 
            return s
        start,left,right=0,0,0 # init
        
        while (start+int((right-left)/2)<len(s)):
            i,j=0,1 # two pointer, i - repeat chars, j - palindrome step
            while (start+i<len(s)-1): # find the repeat chars amount start+i+1<=len(s)-1
                if s[start]==s[start+i+1]: 
                    i+=1
                else: 
                    break  
            while(start-j>=0 and start+i+j<len(s)): # find the number of palindrome step
                if s[start-j]==s[start+i+j]:
                    j+=1
                else: 
                    break
            if (right-left<i-1+2*j):
                left,right=start-j+1,start+j+i
                start=start+i+1
        return s[left:right]