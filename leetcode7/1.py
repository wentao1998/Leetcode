class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        str_x=str(x)   #转化为字符串
        x=''     #定义一个初始字符串，也就是最后输出的字符串
        if str_x[0]=='-':   #存在符号就加入x
            x+='-'
        x+=str_x[len(str_x)-1::-1].lstrip("0").rstrip("-")  #如果有0去掉反转后的首个0和去掉尾部的负号，print str[::-1] #创造一个与原字符串顺序相反的字符串
        x=int(x)
        if -2**31<x<2**31-1:  #判断是否溢出
            return x
        return 0

if __name__=="__main__":
    x=-123
    print(Solution().reverse(x))