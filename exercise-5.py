def reverse_ascending(items):
    # Create an empty list to store the result
    result = []
    
    # Initialize variables to keep track of the current ascending subsequence
    subsequence = []
    prev_num = None
    
    # Iterate through each element in the input list
    for num in items:
        # Check if the current number is greater than the previous number (strictly ascending)
        if prev_num is None or num > prev_num:
            # If it is, add it to the current ascending subsequence
            subsequence.append(num)
        else:
            # If it's not strictly ascending, reverse the subsequence and add it to the result
            result.extend(subsequence[::-1])
            # Start a new ascending subsequence with the current number
            subsequence = [num]
        
        # Update the previous number to the current number for the next iteration
        prev_num = num
    
    # After the loop, add the last ascending subsequence (if any) to the result
    result.extend(subsequence[::-1])
    
    # Return the final result
    return result

print(reverse_ascending([]))