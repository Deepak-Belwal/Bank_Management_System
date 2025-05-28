from account import Account

def heapify(accounts, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    if left < n and accounts[left].ph_number > accounts[largest].ph_number:
        largest = left

    if right < n and accounts[right].ph_number > accounts[largest].ph_number:
        largest = right

    if largest != i:
        accounts[i], accounts[largest] = accounts[largest], accounts[i]  # Swap
        heapify(accounts, n, largest)  # ✅ Ensure accounts are passed, not managers

def heap_sort(accounts):
    n = len(accounts)
    for i in range(n // 2 - 1, -1, -1):
        heapify(accounts, n, i)  # ✅ Fix: Use accounts instead of managers

    for i in range(n - 1, 0, -1):
        accounts[i], accounts[0] = accounts[0], accounts[i]  # Swap
        heapify(accounts, i, 0)  # ✅ Fix: Use accounts instead of managers


def binary_search(accounts, ph_number):
    ph_number = str(ph_number).strip()  # ✅ Convert to string first, then strip spaces

    if not ph_number:  # ✅ Check if phone number is empty
        return None  # Return None if input is invalid

    ph_number = int(ph_number)  # ✅ Convert back to integer after validation

    heap_sort(accounts)  # Sort accounts using Heap Sort

    left, right = 0, len(accounts) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if accounts[mid].ph_number == ph_number:
            return accounts[mid]  # ✅ Account found!
        elif accounts[mid].ph_number < ph_number:
            left = mid + 1
        else:
            right = mid - 1
    return None  # Account not found

