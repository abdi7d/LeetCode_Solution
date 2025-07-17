class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

# Time and Space Complexity

# Time Complexity: O(n) – In the worst case, all digits are 9 and we must process each digit.

#Space Complexity: O(1) extra space (excluding the output list), since we modify the list in place (except in the all-9s case, where we create a new list).
