###### 递归版前序遍历  ######

def preorder(root):
    if root == None:
        return []
    else:
        return [root.val] + preorder(root.left) + preorder(root.right)


