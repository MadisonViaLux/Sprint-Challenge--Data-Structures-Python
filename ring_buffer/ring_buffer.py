from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            new_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if new_head == self.current:
                self.current = self.storage.tail

    # we want to check to see if the length has yet been reached
    #
    # if not then we want to add the item to the tail of our storage
    #
    # and set our current to the storage head for reference
    #
    # If it has been reached then we want to remove the current head
    # and replace it with the new item
    #
    # then we are taking and moving the reference of head so we can
    # remove the current value in it's spot and replace it with the
    # new tail value (new item).

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # while the length of the buffer is less lan the storage length
        # it should append the current value and then check to see if
        # it can move to the next value and append that and repeat the
        # process until there is no next
        #
        # if there is no next then it will need to be reset and the value
        # should be placed back to the head

        # TODO: Your code here
        while len(list_buffer_contents) < self.storage.length:
            list_buffer_contents.append(self.current.value)
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = self.storage.head

        print(list_buffer_contents)
        return list_buffer_contents

# Printed example from README to make sure it's working
buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.get()
buffer.append('c')
buffer.get()
buffer.append('d')
buffer.get()
buffer.append('e')
buffer.append('f')
buffer.get()

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
