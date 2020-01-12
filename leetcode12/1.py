class Solution(object):
    def intToRoman(self, num):
        A=["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]  #设立两个列表
        B=[1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        res=""
        for i in range(len(A)-1,-1,-1):  #从后往前遍历，num依次与B中数字比较,range(start,end,step=1):顾头不顾尾
            while num>=B[i]:   #减去B中数字，加上对应的A中字符
                res+=A[i]
                num-=B[i]
        return res

if __name__=="__main__":
    num=1994
    print(Solution().intToRoman(num))
