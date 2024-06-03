def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# Часова складність: 𝑂(𝑛**2)


def stable_counting_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output
# Часова складність: 𝑂(𝑛 + 𝑘), де 𝑘 — діапазон значень елементів.


# Тести для сортування вставками
assert insertion_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]
assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert insertion_sort([]) == []
print("Сортування вставками: всі тести пройдено")


# Тести для стійкого сортування підрахунком
assert stable_counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]
assert stable_counting_sort([1, 4, 1, 2, 7, 5, 2]) == [1, 1, 2, 2, 4, 5, 7]
assert stable_counting_sort([]) == []
assert stable_counting_sort([4, 2, 2, 8, 3, 3, 1, 0]) == [0, 1, 2, 2, 3, 3, 4, 8]
print("Стійке сортування підрахунком: всі тести пройдено")
