def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        print(f"Iteration: {i} ", arr)
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i] 
        
    return arr


no = [24,67,12,64,91]
print("Sorted Array:", selection_sort(no))