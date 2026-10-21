"""Program 38: Find the Missing Number Using XOR."""


def find_missing_number(numbers):
    """Find the missing number in an array using XOR."""
    if not numbers:
        return 0

    min_val = min(numbers)
    if min_val >= 1:
        n = len(numbers) + 1
        xor_sum = 0
        for i in range(1, n + 1):
            xor_sum ^= i
        for num in numbers:
            xor_sum ^= num
        return xor_sum
    else:
        n = len(numbers)
        xor_sum = 0
        for i in range(n + 1):
            xor_sum ^= i
        for num in numbers:
            xor_sum ^= num
        return xor_sum


# Alias for flexible importing
missing_number_xor = find_missing_number


if __name__ == "__main__":
    nums = [3, 0, 1]
    print("Numbers:", nums)
    print("Missing number:", find_missing_number(nums))
