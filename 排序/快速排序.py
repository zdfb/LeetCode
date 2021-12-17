###### 快速排序 ######

def quick_sort(nums):
    def sort(nums, left, right):
        if left < right:
            low = left
            high = right

            temp = nums[low]  # 参考数据

            while low < high:
                # 从尾部找到第一个小于参考数据的数
                while nums[high] >= temp and low < high:  
                    high -= 1
                if nums[high] < temp:
                    nums[low] = nums[high]  # 将high处的值与放在low处, low+1
                    low += 1
                # 从尾部找到第一个小于参考数据的数
                while nums[low] <= temp and low < high:
                    low += 1
                if nums[low] > temp:
                    nums[high] = nums[low]
                    high -= 1  # 将low处的值放在high处， high-1
            nums[low] = temp # 将参考值放在low处

            sort(nums, left, low - 1)  # 左边递归调用
            sort(nums, high + 1, right) # 右边递归调用
    sort(nums, 0, len(nums) - 1)  # 调用递归函数
