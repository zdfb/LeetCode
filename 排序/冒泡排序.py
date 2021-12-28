###### 冒泡排序 ######


def bubble_sort(nums):
    length = len(nums)  # 数组的长度
    
    for i in range(length):
        for j in range(length - i - 1):
            if a[j + 1] < a[j]:
                a[j], a[j+1] = a[j + 1], a[j]
