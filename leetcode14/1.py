class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 暴力解法,先找出字符串中长度最短的那个，找到位置s，以及长度
        res = ""
        a = 9999999
        for i in range(len(strs)):
            if a > len(strs[i]):
                a = len(strs[i])
                s = i
        #设立一个flag表示所在位置的字符串是否与所有字符串相同，若相同则flag等于1
        flag = 0
        for j in range(a):
            for k in range(len(strs)):
                if strs[s][j] == strs[k][j]:
                    flag = 1
                else:
                    return res
            if flag == 1:    #若flag为1，则加上这个字符
                res += strs[s][j]
        return res


if __name__=="__main__":
    strs=["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))

