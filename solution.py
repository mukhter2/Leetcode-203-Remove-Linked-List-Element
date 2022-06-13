class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        mainList=dummy
        val=-1000
        while head is not None:
            if head.val != val:
                val=head.val
                mainList.next=ListNode(val)
                mainList=mainList.next
            head=head.next
        return dummy.next
