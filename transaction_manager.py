from manager import Manager

# Heap Sort for sorting managers by ID
def mheapify(managers, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and managers[left].manager_id > managers[largest].manager_id:
        largest = left

    if right < n and managers[right].manager_id > managers[largest].manager_id:
        largest = right

    if largest != i:
        managers[i], managers[largest] = managers[largest], managers[i]
        mheapify(managers, n, largest)

def heap_sort(managers):
    n = len(managers)
    for i in range(n // 2 - 1, -1, -1):
        mheapify(managers, n, i)

    for i in range(n - 1, 0, -1):
        managers[i], managers[0] = managers[0], managers[i]
        mheapify(managers, i, 0)

# Binary Search for Manager Login
def binary_search_manager(managers, manager_id):
    heap_sort(managers)  # Sort managers before searching

    left, right = 0, len(managers) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if managers[mid].manager_id == manager_id:
            return managers[mid]  # Manager found!
        elif managers[mid].manager_id < manager_id:
            left = mid + 1
        else:
            right = mid - 1
    return None  # Manager not found