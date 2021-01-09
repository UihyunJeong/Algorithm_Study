
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

'''
Runtime: 116 ms, faster than 5.66% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.4 MB, less than 10.66% of Python3 online submissions for Add Two Numbers.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        now_l1 = l1
        now_l2 = l2
        is_over = False
        
        first_node = ListNode()
        now_result = first_node
        
        while True :
            tmp_sum = now_l1.val + now_l2.val + is_over
            
            if tmp_sum >= 10:
                tmp_sum -= 10
                is_over=True
            else :
                is_over=False
                
            now_result.val = tmp_sum
            
            if now_l1.next and now_l2.next :
                now_l1 = now_l1.next
                now_l2 = now_l2.next
                now_result.next = ListNode()
                now_result = now_result.next
            else :
                if now_l1.next :
                    least_l = now_l1.next
                elif now_l2.next :
                    least_l = now_l2.next
                else :
                    least_l = None
                break
        
        if least_l :
            while True :
                now_result.next = ListNode()
                now_result = now_result.next
                tmp_sum = least_l.val + is_over
                if tmp_sum >= 10:
                    tmp_sum -= 10
                    is_over=True
                else :
                    is_over=False
                now_result.val = tmp_sum
                
                least_l = least_l.next
                if least_l is None :
                    break
            
        if is_over :
            now_result.next = ListNode(1,None)
        
        
        return first_node
                
