def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
# Часова складність: 𝑂(𝑛**2)


def counting_sort(arr):
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)
    return sorted_arr
# Часова складність: 𝑂(𝑛 + 𝑘), де 𝑘 — діапазон значень елементів.

# Тести для сортування вибором
assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]
assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert selection_sort([]) == []
print("Сортування вибором: всі тести пройдено")


# Тести для сортування підрахунком
assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]
assert counting_sort([1, 4, 1, 2, 7, 5, 2]) == [1, 1, 2, 2, 4, 5, 7]
assert counting_sort([]) == []
assert counting_sort([4, 2, 2, 8, 3, 3, 1, 0]) == [0, 1, 2, 2, 3, 3, 4, 8]
print("Сортування підрахунком: всі тести пройдено")

