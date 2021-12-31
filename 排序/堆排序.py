######## 堆排序 ########

# 检查节点是否满足堆，若不满足，递归进行调整
def transfer_heap(heap, heap_length, index):
    root = index  # 根节点
    left = 2 * index + 1  # 该根节点的左节点
    right = left + 1  # 该根节点的右节点

    larger = root  # 最大值索引，初始化为根

    # 判断左节点是否小于根节点
    if left < heap_length and heap[larger] < heap[left]:
        larger = left
    # 判断右节点是否小于根节点
    if right < heap_length and heap[larger] < heap[right]:
        larger = right
    
    if larger != root:  # 若最大值不是根节点
        heap[root], heap[larger] = heap[larger], heap[root]  # 将根节点的值调换为最大值
        transfer_heap(heap, heap_length, larger)  # 递归维护调换后的节点


# 建立大根堆
def build_heap(heap):
    heap_length = len(heap)

    # 从第num_length / 2 个节点开始遍历，使之遵循大根堆的规则
    for index in range(heap_length // 2, -1, -1):
        transfer_heap(heap, heap_length, index)

# 进行排序
def heap_sort(heap):
    build_heap(heap)
    for index in range(len(heap) - 1, -1, -1):
        heap[0],heap[index] = heap[index],heap[0]  # 将堆顶元素与最后一个元素进行调换
        transfer_heap(heap, index, 0)  # 从堆顶开始维护