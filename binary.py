class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data


    def PrintTree(self):
        print(self.data)

root = Node('+')
root.left=Node(3)
root.right=Node(4)

def calc(node: Node):
  if node.data=='+':
    return calc(node.left)+calc(node.right)
  
  return node.data


print(calc(root))
