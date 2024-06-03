def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# Оригінальний тест
arr = [2, 3, 4, 10, 40]
x = 10
print(f"Index of {x}:", binary_search(arr, 0, len(arr)-1, x))  # Output: 3

# Додаткові тести
# Тест 1: елемент знаходиться на початку масиву
arr = [1, 3, 5, 7, 9]
x = 1
print(f"Index of {x}:", binary_search(arr, 0, len(arr)-1, x))  # Output: 0

# Тест 2: елемент знаходиться в кінці масиву
arr = [1, 3, 5, 7, 9]
x = 9
print(f"Index of {x}:", binary_search(arr, 0, len(arr)-1, x))  # Output: 4

# Тест 3: елемент відсутній у масиві
arr = [1, 3, 5, 7, 9]
x = 4
print(f"Index of {x}:", binary_search(arr, 0, len(arr)-1, x))  # Output: -1

# Тест 4: масив з одним елементом
arr = [8]
x = 8
print(f"Index of {x}:", binary_search(arr, 0, len(arr)-1, x))  # Output: 0

# Тест 5: масив з двома елементами, шукаємо перший
arr = [4, 8]
x = 4
print(f"Index of {x}:", binary_search(arr, 0, len(arr)-1, x))  # Output: 0

# Тест 6: масив з двома елементами, шукаємо другий
arr = [4, 8]
x = 8
print(f"Index of {x}:", binary_search(arr, 0, len(arr)-1, x))  # Output: 1

# Тест 7: порожній масив
arr = []
x = 1
print(f"Index of {x}:", binary_search(arr, 0, len(arr)-1, x))  # Output: -1
