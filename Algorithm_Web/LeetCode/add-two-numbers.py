'''
update : 21.01.09
url : https://leetcode.com/problems/add-two-numbers/

category : greedy
@copyright : UihyunJeong
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_num(l : ListNode) -> int:
            num = ''
            now_node = l
            while True :
                num = str(now_node.val) + num
                if not now_node.next :
                    break
                else :
                    now_node = now_node.next
            return num
        
        sum_val = str(int(get_num(l1))+int(get_num(l2)))[::-1]
        first_node = ListNode()
        now_node = first_node
        idx = 0
        while True :
            now_node.val = sum_val[idx]
            if idx == len(sum_val)-1 :
                break
            else :
                now_node.next = ListNode()
                now_node = now_node.next
                idx+=1

                
        return first_node
