def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
# Часова складність: 𝑂(𝑛)


def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
# Часова складність: 𝑂(log⁡ 𝑛)


# Тести для лінійного пошуку
assert linear_search([1, 2, 3, 4, 5], 3) == 2
assert linear_search([1, 2, 3, 4, 5], 6) == -1
assert linear_search([], 3) == -1
assert linear_search([5, 4, 3, 2, 1], 1) == 4
print("Лінійний пошук: всі тести пройдено")

# Тести для двійкового пошуку
assert binary_search([1, 2, 3, 4, 5], 3) == 2
assert binary_search([1, 2, 3, 4, 5], 6) == -1
assert binary_search([], 3) == -1
assert binary_search([1, 2, 3, 4, 5], 1) == 0
print("Двійковий пошук: всі тести пройдено")
