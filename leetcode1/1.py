def twoSum(nums, target):
    n=len(nums)
    for i in range(n):
        temp=nums[:]
        temp[i]='#'
        dif=target-nums[i]
        if dif in temp:
            return [i,temp.index(dif)]
    return []

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    s=twoSum(nums,target)
    print(s)