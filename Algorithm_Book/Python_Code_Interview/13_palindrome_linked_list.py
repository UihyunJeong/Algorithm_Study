# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ''' 
        # Runtime: 152 ms, faster than 5.68% of Python3 online submissions for Palindrome Linked List.
        # Memory Usage: 24.4 MB, less than 47.55% of Python3 online submissions for Palindrome Linked List.
        q  = []
        
        if not head :
             return True
            
        node = head
        while node is not None :
            q.append(node.val)
            node = node.next
        
        return True if q == q[::-1] else False
        '''
        
        '''
        # Runtime: 68 ms, faster than 75.17% of Python3 online submissions for Palindrome Linked List.
        # Memory Usage: 24.4 MB, less than 30.40% of Python3 online submissions for Palindrome Linked List.
        q = collections.deque()
        if not head :
             return True
            
        node = head
        while node is not None :
            q.append(node.val)
            node = node.next
        
        while len(q) > 1 :
            if q.popleft() != q.pop():
                return False
        
        return True
        '''
        
        '''
        runner 개념
        Runtime: 76 ms, faster than 32.68% of Python3 online submissions for Palindrome Linked List.
        Memory Usage: 24.5 MB, less than 30.40% of Python3 online submissions for Palindrome Linked List.

        '''
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev , slow.next
        
        if fast :
            slow = slow.next
        
        while rev and rev.val==slow.val :
            rev, slow = rev.next, slow.next 
        
        return not rev
