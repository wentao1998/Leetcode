class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        x=str(x)  #转化为字符串处理
        n=len(x)
        for i in range(n):
            if x[i]!=x[n-i-1]:
                return False
        return True

if __name__=="__main__":
    x=10
    print(Solution().isPalindrome(x))