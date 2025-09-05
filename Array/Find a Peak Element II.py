class Solution:
    def findPeakGrid(self, rat: list[list[int]]) -> list[int]:
        result = []
 
        m = len(rat)
        for r in rat:
            n = len(rat[m-1])
            left = 0
            right =n-1
            top = 0
            buttor =m-1
            # out perireter with the value -1
            # if rat
            for c in r:
                # corpare with left elerent
                while (left<right) and (top<buttor):
                    if (r[c]>r[left]) and (r[c]>r[right]):
                        if (r[c]>r[top]) and (r[c]>r[buttor]):
                            result= [r,c]
                        else:
                            left +=1
                            top +=1
        return result


mat = [[1,4], [3,2]]
abdi = Solution()
abdi.findPeakGrid(mat)
# rat = [[1, 4], [3, 2, 3], [4, 5]]

'''  
# print(len(rat)) # this reans how rany rows this ratrix have --- 3
kana jechuun rat kan jedharu kun row reeqa qabaa jechuudha.
'''



'''
# print(len(rat[1])) # row'n larraffaaan elerent reeqa qabaa ---- 3
kana jechuun row'n kan index'n isaa 1 ta'e elerent reeqa qabaa jechuudha.
'''