class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=0
        if len(s) == 0:  # 字符串长度为0，返回0
            return 0
        st = ''
        length = 0  # 设定变量length
        num = []  # 设定一个列表存储长度
        for i in range(len(s)):  # 遍历字符串
            if s[i] not in st:  # 如果在st中找不到遍历到的字符，则st加上这个字符，同时存储此时st的长度
                st += s[i]
                num.append(len(st))
            else:
                st = st[st.find(s[i]) + 1:] + s[i]  # 如果st有与字符重复，则找到重复位置，对重新st重新取值
        return max(num)  # 返回num存储的最大数字

if __name__ == '__main__':
    str="abcabcbb"
    a=Solution().lengthOfLongestSubstring(str)
    print(a)