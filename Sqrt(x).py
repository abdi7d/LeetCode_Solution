class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # Return 0 or 1 directly

        left, right = 2, x // 2  # Initialize binary search bounds

        while left <= right:
            mid = left + (right - left) // 2
            mid_squared = mid * mid

            if mid_squared == x:
                return mid  # Exact square root found
            elif mid_squared < x:
                left = mid + 1  # Move to the upper half
            else:
                right = mid - 1  # Move to the lower half

        return right  # Return the floor of the square root



