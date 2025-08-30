class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:

        result = []
        first_element =0
        last_element = len(mountain)-1

        for i in range(len(mountain)):
            if i ==first_element or i ==last_element:
                continue
            else:
                prev= i-1
                next= i+1
                if  (mountain[prev] < mountain[i]) and (mountain[next] < mountain[i]):
                    result.append(i)
        return result

'''
Time and Space Complexity


'''