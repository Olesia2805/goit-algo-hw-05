def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iter = 0
    result = None
 
    while low <= high:
 
        mid = (high + low) // 2
        iter += 1

        if arr[mid] < x:
            low = mid + 1
            
        elif arr[mid] > x:
            result = arr[mid]
            high = mid - 1
 
        else:
            return arr[mid]
 
    return result

arr = [10.5, 15.7, 20.9, 25.1, 30.3, 35.5, 40.7, 45.9, 50.1, 55.3, 60.5, 65.7, 70.9, 76.1, 81.3, 86.5, 91.7, 96.9, 102.1, 107.3]

result1 = binary_search(arr, 108)
result2 = binary_search(arr, 81.3)
result3 = binary_search(arr, 14)
result4 = binary_search(arr, 5)


print(f"Result {result1}") if result1 != None else print("Element is not present in array")
print(f"Result {result2}") if result2 != None else print("Element is not present in array")
print(f"Result {result3}") if result3 != None else print("Element is not present in array")
print(f"Result {result4}") if result4 != None else print("Element is not present in array")
