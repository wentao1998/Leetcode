class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0  #设立左右指针
        right=len(height)-1
        maxs=min(height[left],height[right])*(right-left)  #算出最左和最右的水量
        while left<right:    #指针向中间移动
            if height[left]<height[right]:   #如果左边高度小，则左边移动，反之
                left+=1
            else:
                right-=1
            maxs=max(maxs,min(height[left],height[right])*(right-left))  #比较，更新最大值
        return maxs

if __name__=="__main__":
    height=[1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))