'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    ''' FIRST PASS SOLUTION '''

    # # Look for the maximum value within k throughout the nums arr and store those values in a result list
    # result = []
    # index = 0
    # end_index = k

    # # If len(k) - 1 > len(nums) - 1 return because the sliding window is no longer fitting within the list
    # while index <= len(nums) - k:
    #     # Start at index 0 and create a subarray of len k (slice nums to be nums[index:k])
    #     temp_nums = nums[index:end_index]
    #     max_value = max(temp_nums)
    #     result.append(max_value)

    #     # After each pass increment indexes by 1
    #     index += 1
    #     end_index += 1

    # return result

    ''' WRITING BETTER SOLUTIONS '''

    result = []

    # Loop through nums using enumerate to get index at each element
    for idx,e in enumerate(nums):
        # Create temp list for nums sliced between index and index + k
        temp_list = nums[idx:idx + k]

        # If len(temp_list) < k, break loop
        if len(temp_list) < k:
            break
        # Else, find max from that list and append to result list
        else:
            max_value = max(temp_list)
            result.append(max_value)

    return result

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
