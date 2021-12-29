###### 迭代版后序遍历 ######


def postorder(root):
    p = root
    stack = []  # 用于存储中间节点
    result = []  # 最终输出结果
    pre = None  # 记录遍历过的节点

    while p != None or len(stack) != 0:
        if p == None:
            p = stack[-1]
            stack[:-1]
            if p.right == None or p.right == pre:
                result.append(p.val)
                pre = p
                p = None
            else:
                stack.append(p)
                p = p.right
        else:
            stack.append(p)
            p = p.left
    return result
