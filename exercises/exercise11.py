# Exercise 11: Bubble Sort
# Write a function that sorts a list using bubble sort algorithm.
# Example: bubble_sort([64, 34, 25, 12, 22, 11, 90]) should return [11, 12, 22, 25, 34, 64, 90]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test the function
if __name__ == "__main__":
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # Expected: [11, 12, 22, 25, 34, 64, 90]
