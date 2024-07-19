def merge_sort(arr):
    arr_len = len(arr)
    if arr_len == 1:
        return arr

    sorted1_len = arr_len // 2
    sorted2_len = arr_len - sorted1_len

    sorted1 = merge_sort(arr[:sorted1_len])
    sorted2 = merge_sort(arr[sorted1_len:])

    res = []
    i = 0
    j = 0
    while i < sorted1_len and j < sorted2_len:
        if sorted1[i] < sorted2[j]:
            res.append(sorted1[i])
            i += 1
        else:
            res.append(sorted2[j])
            j += 1
    
    if i == sorted1_len:
        while j < sorted2_len:
            res.append(sorted2[j])
            j += 1
    else:
        while i < sorted1_len:
            res.append(sorted1[i])
            i += 1
    
    return res
