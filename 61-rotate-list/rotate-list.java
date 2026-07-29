class Solution{
    public ListNode rotateRight(ListNode head,int k){
        if(head==null||head.next==null||k==0) return head; // edge

        int len=1;
        ListNode tail=head;
        while(tail.next!=null){ tail=tail.next; len++; } 

        k%=len;
        if(k==0) return head; 

        tail.next=head; // circular

        int steps=len-k;
        ListNode newtail=head;
        for(int i=1;i<steps;i++) newtail=newtail.next; 

        ListNode newhead=newtail.next; // head
        newtail.next=null;

        return newhead;
    }
}