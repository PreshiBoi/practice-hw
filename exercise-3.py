def remove_all_after(numbers, n):
    if len(numbers) == 0: 
        return []
    
    for i, index in enumerate(numbers):  
        if index == n:
            return numbers[:i+1]
    
    return numbers  

