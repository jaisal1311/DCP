# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def __init__(self):
        self.nodes = []
    
    def serialize(self, root):
        if not root:
            self.nodes.append('null')
            
        else:
            self.nodes.append(str(root.val))

            self.serialize(root.left)
            self.serialize(root.right)

        return ",".join(self.nodes)
    
    def deserializeHelper(self, queue):
        val = queue.popleft()
        
        if val == 'null':
            return None
        
        root = TreeNode(int(val))
        root.left = self.deserializeHelper(queue)
        root.right = self.deserializeHelper(queue)
        
        return root
    
    def deserialize(self, data):
        queue = deque(data.split(','))
        return self.deserializeHelper(queue)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
