# Exercise 10: Sort a List
# Write a function that sorts a list in ascending order.
# Example: sort_list([3, 1, 4, 1, 5]) should return [1, 1, 3, 4, 5]

def sort_list(lst):
    return sorted(lst)

# Test the function
if __name__ == "__main__":
    print(sort_list([3, 1, 4, 1, 5]))  # Expected: [1, 1, 3, 4, 5]
