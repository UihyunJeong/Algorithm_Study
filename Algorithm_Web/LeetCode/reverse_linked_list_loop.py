class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
#         def reverse(node: ListNode, prev: ListNode=None) :
#             if node is None :
#                 return prev
#             next_node, node.next = node.next, prev
            
#             return reverse(next_node, node)
        
#         return reverse(head)

        node, prev = head, None
    
        while node :
            next_node, node.next = node.next, prev
            prev, node = node, next_node
        
        return prev
