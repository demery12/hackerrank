# Need to add memoization to speed this up, but I want to get in before midnight
def maxSubsetSum(arr):
    if len(arr)<3:
        max_arr[arr] = max(arr)
    return max(arr[0] + maxSubsetSum(arr[2:]), maxSubsetSum(arr[1:]))
