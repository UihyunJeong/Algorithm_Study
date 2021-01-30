class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        root=head=ListNode(-1)
        carry = 0
        while l1 or l2 or carry :
            sum_val = 0
            if l1 :
                sum_val+=l1.val
                l1 = l1.next
            
            if l2 :
                sum_val+=l2.val
                l2 = l2.next
            
            carry, val = divmod(sum_val+carry, 10)
            head.next = ListNode(val)
            head = head.next
            
        
        return root.next    
  
 # 연결리스트에서 초기값을 None으로 하고 매번 체크하느 것 보다 미리 ListNode를 넣어두고 리턴을 root.next부터하면 가독성과 효율성이 좋다
