def find_duplicate(nums):
    if len(nums) < 2 or not all(
        isinstance(num, int) and num >= 0 for num in nums
    ):
        return False

    unique_values = set()
    for num in nums:
        if num in unique_values:
            return num
        unique_values.add(num)

    return False
