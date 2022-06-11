

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        rootp = None                        # set parent of root to none
        while root and root.next:
            p1, p2 = root, root.next        # two pointers to slide 
            while p2 and p1.val == p2.val:  # loop until duplicates are found
                p2 = p2.next
            if p2 == root.next:             # set rootp if no duplicates where found
                rootp = p1
            if rootp:                       # if rootp exists, cut all the duplicates in b/w 
                rootp.next = p2
            else: 
                head = p2                   # else head needs to be shifted
            root = p2
        return head


# [1,1,1,2,3] -> [2,3]
# [1, 2, 3, 3, 3, 4, 4] -> [1,2]