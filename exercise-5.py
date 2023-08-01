def reverse_ascending(numbers):
    lists = []
    for i in numbers:
        lists.append(i)
    return sorted(lists, reverse = True)
    
print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))
