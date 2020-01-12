class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #转化为两数之和，采用取出一个数，再用0减除这个数，记为target，再查找列表是否存在target
        L,res= len(nums),[]
        nums.sort()           #先对列表进行排序
        for i in range(L-2):    #一直遍历到倒数第三个数字
            if i>0 and nums[i]==nums[i-1]:  #如果遍历到的数字（取出的那个），后面一个和前面的相同的话，可以跳过一轮循环，节约时间
                continue
            target=0-nums[i]
            j,k=i+1,L-1
            while j<k:     #找后面两个数字，一直遍历到j等于k
                if nums[j]+nums[k]==target:
                    res.append([nums[i],nums[j],nums[k]])   #找到目标，同时j向右移动
                    j+=1
                    while j<k and nums[j]==nums[j-1]:  #同上面的优化，后面一个和前面的相同的话，可以跳过，节约时间
                        j+=1
                elif nums[j]+nums[k]<target:   #如果相加比target小的话，说明加起来不够大，所以需要j向右移动
                    j+=1
                else:
                    k-=1   #同理，大了，k就向左移动
        return res


if __name__=="__main__":
    nums=[-1,0,1,2,-1,-4]
    print(Solution().threeSum(nums))