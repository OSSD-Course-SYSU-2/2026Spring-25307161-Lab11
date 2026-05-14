def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # 遍历数组从 0 到 n-i-1
            # 交换如果元素大于下一个元素
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 测试代码
if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    print("原始列表:", my_list)
    sorted_list = bubble_sort(my_list)
    print("排序后列表:", sorted_list)