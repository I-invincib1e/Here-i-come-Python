# Exercise 12: Binary Search
# Write a function that performs binary search on a sorted list.
# Example: binary_search([1, 3, 5, 7, 9], 5) should return 2

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test the function
if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9], 5))  # Expected: 2
    print(binary_search([1, 3, 5, 7, 9], 6))  # Expected: -1
