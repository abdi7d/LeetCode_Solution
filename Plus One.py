class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                break
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
        
        if carry == 1:
            digits.insert(0, 1)
        
        return digits

# example usage
if __name__ == "__main__":  
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
    print(solution.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]
    print(solution.plusOne([0]))        # Output: [1]
    print(solution.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]