def maxFrequency(nums, k):
    nums.sort()
    maxFreq = 0
    currFreq = 0
    start = 0
    operations = 0

    for end in range(len(nums)):
        currFreq += 1
        operations += nums[end]

        while nums[end] * currFreq > operations + k:
            operations -= nums[start]
            currFreq -= 1
            start += 1

        maxFreq = max(maxFreq, currFreq)

    return maxFreq

# Example usage:
print(maxFrequency([3,9,6], 2))  # Output: 3
