class ListNode(object):
    def __init__(self, x):
               self.val = x
               self.next = None

class Solution:
    def addTwoNumbers(self,l1, l2):
        temp=ListNode(0)
        l3=temp
        a=0
        while l1!=None or l2!=None or a!=0:
            if l1!=None:
                a+=l1.val
                l1=l1.next
            if l2!=None:
                a+=l2.val
                l2=l2.next
            temp.next=ListNode(a%10)
            temp=temp.next
            a=a//10
        return l3.next

def printList(l):
    while(True):
        print(l.val)
        if l.next is not None:
            l = l.next
        else:
            print()
            break


if __name__ == '__main__':
    # 342 + 465 = 807
    l1_1 = ListNode(3)
    l1_2 = ListNode(4)
    l1_3 = ListNode(2)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(4)
    l2_2 = ListNode(6)
    l2_3 = ListNode(5)
    l2_1.next = l2_2
    l2_2.next = l2_3

    l3 = Solution().addTwoNumbers(l1_1, l2_1)
    printList(l3)
