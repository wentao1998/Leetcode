#中心拓展法。扫一遍字符串s，对于回文子串长为奇数的情况，求s[i]为轴对称中心的回文子串最长值；回文子串长偶数的情况，求s[i]与s[i+i] 为中心的最长值。
# 最后求最长。时间复杂度o(n^2)，因为扫一遍o(n)，中心扩展也是o(n)。注意数组越界和下标
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = end = 0

        for i in range(len(s)):
            len1 = self.centerexpand(s, i, i)  # 回文串长度为奇数，aba
            len2 = self.centerexpand(s, i, i + 1)  # 回文串长度为偶数，abba
            maxlen = max(len1, len2)
            if maxlen > end - start + 1:
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2
        return s[start: end + 1]

    def centerexpand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:  #从中间往两边拓展，如果字符一样，则l 减一，r加1
            l -= 1
            r += 1
        return r - l - 1  #返回结尾减去开头的长度

if __name__=='__main__':
    s="LEETCODEISHIRING"
    print(Solution().longestPalindrome(s))