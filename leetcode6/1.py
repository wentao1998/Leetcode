class Solution:
    def convert(self, s, numRows):
        result = ['']*min(numRows,len(s))  #用字符串的个数模拟行数，假如是三行，则设定三个字符串，一个表示一行,如['', '', '']
        #print(result)
        current_row = 0  #记录现在的行数
        go_up_down = 0   #设定一个方向
        if len(s)<=1 or numRows<=1:
            return s
        else:
            for i in range(len(s)):
                result[current_row] = result[current_row] + s[i]    #字符进入现在的行数
                if current_row == 0:      #如果现在行数是第一行，则方向向下
                    go_up_down = 1
                elif current_row == numRows -1:   #如果现在的行数是最后一行，则方向向上
                    go_up_down = -1
                current_row = current_row + go_up_down   #移动行数
        #print(''.join(result))
        return ''.join(result)   #将字符串连接起来

if __name__=='__main__':
    s="LEETCODEISHIRING"
    print(Solution().convert(s,3))