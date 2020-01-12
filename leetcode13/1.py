class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #首先建立一个HashMap来映射符号和值，然后对字符串从左到右来，
        # 如果当前字符代表的值不小于其右边，就加上该值；否则就减去该值。
        # 以此类推到最左边的数，最终得到的结果即是答案
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res=0
        for i in range(len(s)):
            if i<len(s)-1 and d[s[i]]<d[s[i+1]]:
                res-=d[s[i]]
            else:
                res+=d[s[i]]
        return res



if __name__=="__main__":
    s="LVIII"
    print(Solution().romanToInt(s))