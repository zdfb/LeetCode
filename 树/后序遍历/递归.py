###### 递归版后序遍历 ######


def postorder(root):
    if root == None:
        return []
    else:
        return postorder(root.left) + postorder(root.right) + [root.val]
