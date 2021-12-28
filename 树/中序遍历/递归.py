###### 递归版中序遍历  ######

def inorder(root):
    if root == None:
        return []
    else:
        return inorder(root.left) + [root.val] + inorder(root.right)

    