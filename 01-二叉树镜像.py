class Solution:
    def Mirror(self,root):

        if root == None:
            return 0
        self.Mirror(root.left)
        self.Mirror(root.right)
        root.left ,root.right = root.right ,root.left