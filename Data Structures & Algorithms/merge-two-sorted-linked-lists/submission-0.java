/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode curr2 = list2;

        while (curr2 != null) {

            ListNode next2 = curr2.next;   // save next node of list2

            ListNode curr1 = list1;
            ListNode prev = null;

            // iterate list1 to find insert position
            while (curr1 != null && curr1.val < curr2.val) {
                prev = curr1;
                curr1 = curr1.next;
            }

            // insert curr2
            if (prev == null) {
                // insert at head (left of list1)
                curr2.next = list1;
                list1 = curr2;
            } else {
                // insert between prev and curr1
                prev.next = curr2;
                curr2.next = curr1;
            }

            curr2 = next2; // move to next node in list2
        }

        return list1;
    }
}