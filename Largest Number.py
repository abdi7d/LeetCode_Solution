class Solution:
    def largestNumber(self, nums):
        # Convert numbers to strings for easy comparison
        nums_str = list(map(str, nums))
        
        # Sort numbers based on which combination is larger
        nums_str.sort(key=lambda x: x*10, reverse=True)
        
        # Join sorted strings into the largest number
        largest_num = ''.join(nums_str)
        
        # Handle the case where the result is '0'
        # Check if the first character of the largest number is '0'
        if largest_num[0] != '0':
            return largest_num  # If it's not '0', return the largest number
        else:
            return '0'  # If it is '0', return '0'

# Example usage :
solution = Solution()
print(solution.largestNumber([10, 2]))  # Output: "210"
print(solution.largestNumber([3, 30, 34, 5, 9]))  # Output: "9534330"