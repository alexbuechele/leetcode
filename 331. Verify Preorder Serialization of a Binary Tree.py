# 331. Verify Preorder Serialization of a Binary Tree

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        child_stack = 1
        entries = preorder.split(',')
        
        preorder_length = len(entries)
        
        if preorder_length % 2 != 1:
            return False
        
        
        
        for index, node in enumerate(entries):
            if node == '#':
                child_stack -= 1
            else: 
                child_stack += 1
            if child_stack < 0 or (child_stack == 0 and index != preorder_length - 1):
                return False
        if child_stack != 0:
            return False
        return True
        
