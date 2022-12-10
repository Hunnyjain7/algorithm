def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        left_arr_idx = 0
        right_arr_idx = 0
        merge_arr_idx = 0
        while left_arr_idx < len(left_arr) and right_arr_idx < len(right_arr):
            if left_arr[left_arr_idx] < right_arr[right_arr_idx]:
                arr[merge_arr_idx] = left_arr[left_arr_idx]
                left_arr_idx += 1
            else:
                arr[merge_arr_idx] = right_arr[right_arr_idx]
                right_arr_idx += 1
            merge_arr_idx += 1

        while left_arr_idx < len(left_arr):
            arr[merge_arr_idx] = left_arr[left_arr_idx]
            left_arr_idx += 1
            merge_arr_idx += 1

        while right_arr_idx < len(right_arr):
            arr[merge_arr_idx] = right_arr[right_arr_idx]
            right_arr_idx += 1
            merge_arr_idx += 1


a = [9683, 1154, 8494, 9560, 3268, 7814, 9956, 654, 4141, 5449, 6317, 5526, 5978, 9749, 3977, 9315, 5253, 2387, 4151]
merge_sort(a)
print(a)
