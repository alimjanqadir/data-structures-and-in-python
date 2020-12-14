class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.list = []
        self.head = 0
        self.tail = 0

    def insert(self, node: Node, position=-1):
        if len(self.list) == 0:
            self.list.append(node)
        elif position == -1:
            previous_node = self.list[len(self.list) - 1]
            previous_node.next = node
            self.list.append(node)
        else:
            temp = self.list[position]
            previous_node = self.list[position - 1]
            previous_node.next = node
            node.next = temp
        self.tail += 1

    def remove(self):
        pass

    def print_list(self):
        while self.head < self.tail:
            node = self.list[self.head]
            print(node.value)
            self.head += 1


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.next = b
b.next = c
a.next = b
a.next = b

linked_list = LinkedList()
linked_list.insert(a)
linked_list.insert(b)
linked_list.insert(c)
linked_list.insert(d)
linked_list.print_list()
