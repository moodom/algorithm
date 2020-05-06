# 打印两个有序链表的公共部分
# 给定两个有序链表的头指针head1和head2,打印两个链表的公共部分

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class PrintCommonPart:
    def printcommonpart(self,head1,head2):
        while head1 and head2:
            if head1==head2:
                while head1:
                    print(head1.val)
                    head=head.next
            elif head1.val<head2:
                head1=head1.next
            else:
                head2=head2.next
            
    
        
