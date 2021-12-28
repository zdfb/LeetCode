###### 迭代版前序遍历  ######

def preorder(root):
    p = root  # 哨兵节点
    stack = []  # 用于存储中间节点的栈
    result = []  # 用于存储遍历结果

    while p != None or len(stack) != 0:
        if p == None:
            p = stack[-1].right
            stack = stack[:-1]
        else:
            result.append(p.val)
            stack.append(p)
            p = p.left
    return result