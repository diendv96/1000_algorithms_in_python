import LinkedList


class LinkedList(LinkedList.LinkedList):
    """
    Time: O(n)
    Space: O(n)
    """

    def print_kth_to_last_recursive(self, head, k):
        if not head:
            return 0

        index = self.print_kth_to_last_recursive(head.next, k) + 1

        if index == k:
            print(str(k) + "th to last node is " + str(head.data))
        return index

    """
    Time: O(n)
    Space: O(1)
    """

    def print_kth_to_last_loop(self, kth):
        p1 = self.head
        p2 = self.head

        # Check k is negative, not exists
        if kth <= 0:
            return

        for x in range(1, kth):
            p1 = p1.next

            # If k is greater than length of linked list, exit, not exist
            if not p1:
                return

        while p1 and p1.next:
            p1 = p1.next
            p2 = p2.next

        print(str(kth) + "th to last node is " + str(p2.data))


inputs = [1, 10, 2, 5, 7, 3, 20, 9, 8, 4, 100]
k = LinkedList()
for number in inputs:
    k.insert(number)

print(k)
k.print_kth_to_last_recursive(k.head, 11)
k.print_kth_to_last_loop(11)
