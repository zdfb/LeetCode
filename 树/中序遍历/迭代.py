###### 迭代版中序遍历  ######

def inorder(root):
    p = root  # 哨兵节点
    stack = []  # 存储中间节点的栈
    result = []  # 存储输出结果

    while p != None or len(stack) != 0:
        if p == None:
            p = stack[-1]
            result.append(p.val)
            p = p.right
            stack = stack[:-1]
        else:
            stack.append(p)
            p = p.left
    return result
    