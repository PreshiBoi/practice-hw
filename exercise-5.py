def reverse_ascending(numbers):
    result = []
    subsequence = []
    prev_num = None
    
    for num in numbers:
        if prev_num is None or num > prev_num:
            subsequence.append(num)
        else:
            result.extend(subsequence[::-1])
            subsequence = [num]
        
        prev_num = num
    
    result.extend(subsequence[::-1])
    
    return result

print(reverse_ascending([]))
