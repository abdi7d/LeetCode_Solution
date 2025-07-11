class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        reversed_num = 0
        
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10
        
        if is_negative:
            reversed_num = -reversed_num
        
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num

# Example usage:
solution = Solution()

x1 = 123
print(solution.reverse(x1))  # Output: 321

x2 = -123
print(solution.reverse(x2))  # Output: -321

x3 = 120
print(solution.reverse(x3))  # Output: 21    