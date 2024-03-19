from collections import Counter

def solution(a, b, c, d):
    counts = Counter([a, b, c, d])
    nums = list(counts.keys())
    freqs = list(counts.values())

    if freqs.count(4):
        return 1111 * nums[0]

    elif freqs.count(3):
        p = nums[freqs.index(3)]
        q = nums[freqs.index(1)]
        return (10 * p + q) ** 2

    elif freqs.count(2) == 2:
        return (nums[0] + nums[1]) * abs(nums[0] - nums[1])
    
    elif freqs.count(2) == 1 and len(nums) == 3:
        q, r = [num for num in nums if counts[num] == 1]
        return q * r

    elif len(nums) == 4:
        return min(nums)

    return 0
