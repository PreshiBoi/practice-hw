# In a given list the last element should become the first one. 
# An empty list or list with only one element should stay the same.
# Example:
# replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
# replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
# replace_last([1]) == [1]
# replace_last([]) == []

def replace_last(numbers):
    last_num = numbers[-1:]
    exclude_last_num = numbers[:-1]
    numbers = last_num + exclude_last_num
    return numbers
# print(replace_last([2, 3, 4, 1]))
