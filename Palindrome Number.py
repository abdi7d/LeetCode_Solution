class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Store the original number for comparison
        original_x = x
        reversed_x = 0

        # Reverse the number
        while x > 0:
            digit = x % 10  # Get the last digit
            reversed_x = reversed_x * 10 + digit  # Append the digit to reversed_x
            x //= 10  # Remove the last digit from x

        # Compare the original and reversed numbers
        return original_x == reversed_x

# Example usage:
solution = Solution() 
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121)) # Output: False
