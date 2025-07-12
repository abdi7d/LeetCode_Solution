class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: Negative numbers are not palindromes
        if x < 0:
            return False

        # Step 2: Store the original number
        original_x = x
        reversed_x = 0

        # Step 3: Reverse the number
        while x > 0:
            digit = x % 10  # Extract the last digit
            reversed_x = reversed_x * 10 + digit  # Add digit to reversed number
            x //= 10  # Remove the last digit from x

        # Step 4: Compare the reversed number with the original
        return original_x == reversed_x