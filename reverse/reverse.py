class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # pass
        if node != None:
            next = node.get_next()
            current = node
            if next == None:
                self.head = node
                self.head.set_next(prev)
            self.reverse_list(next, current)
            node.set_next(prev)

        # Learned:
        # I can't plan well without writing by hand first
        # I need to pay attention to methods available
        # order matters



        # current_node = node
        # new_node = self.reverse_list(node.get_next(), current_node)
        # if node.get_next() == None:
        #     self.head = node
        # return new_node