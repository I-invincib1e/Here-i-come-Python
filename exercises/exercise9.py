# Exercise 9: Find Duplicates in a List
# Write a function that finds all duplicate elements in a list.
# Example: find_duplicates([1, 2, 2, 3, 4, 4]) should return [2, 4]

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Test the function
if __name__ == "__main__":
    print(find_duplicates([1, 2, 2, 3, 4, 4]))  # Expected: [2, 4]
