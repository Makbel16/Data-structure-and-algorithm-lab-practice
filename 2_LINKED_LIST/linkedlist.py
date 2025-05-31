
class Node:
    def __init__(self, data):
        self.data = data     
        self.next = None      


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(30)

node1.next = node2
node2.next = node3


now = node1
while now is not None:
    print(now.data)
    now = now.next
     

 