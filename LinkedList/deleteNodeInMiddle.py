import LinkedList


class LinkedList(LinkedList.LinkedList):
    '''
    Implement an algorithm to delete a node in the middle (i.e., any node but
    the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
    that node.
    EXAMPLE
    lnput:the node c from the linked lista->b->c->d->e->f
    Result: nothing is returned, but the new linked list looks like a->b->d->e- >f
    '''

    def delete_node_in_middle(self, node):
        """
        Solution: Example delete 3th node
        - Copy data and next pointer of 4th node and delete the 4th pointer
        - Set 3th node data to 4th data
        - Set 3th node next pointer to 4th next pointer
        :param node:
        :return node_data_deleted:
        """
        if not node.next:
            return

        next_node = node.next
        next_node_data = node.next.data
        node.data = next_node_data
        node.next = next_node.next

        return node


inputs = [1, 10, 2, 5, 7, 3, 20, 9, 8, 4, 100]
k = LinkedList()
for number in inputs:
    k.insert(number)

# delete 3th element (data = 2)
node_to_delete = k.head.next.next
print(k)
print("delete node with data " + str(node_to_delete.data))
k.delete_node_in_middle(node_to_delete)
print(k)
