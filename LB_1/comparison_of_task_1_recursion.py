def recursive_linear_search(arr, x, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == x:
        return index
    return recursive_linear_search(arr, x, index + 1)
# Часова складність: 𝑂(𝑛)


def recursive_binary_search(arr, x, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return recursive_binary_search(arr, x, mid + 1, high)
    else:
        return recursive_binary_search(arr, x, low, mid - 1)
# Часова складність: 𝑂(log⁡ 𝑛)


# Тести для рекурсивного лінійного пошуку
assert recursive_linear_search([1, 2, 3, 4, 5], 3) == 2
assert recursive_linear_search([1, 2, 3, 4, 5], 6) == -1
assert recursive_linear_search([], 3) == -1
assert recursive_linear_search([5, 4, 3, 2, 1], 1) == 4
print("Рекурсивний лінійний пошук: всі тести пройдено")


# Тести для рекурсивного двійкового пошуку
assert recursive_binary_search([1, 2, 3, 4, 5], 3) == 2
assert recursive_binary_search([1, 2, 3, 4, 5], 6) == -1
assert recursive_binary_search([], 3) == -1
assert recursive_binary_search([1, 2, 3, 4, 5], 1) == 0
print("Рекурсивний двійковий пошук: всі тести пройдено")
