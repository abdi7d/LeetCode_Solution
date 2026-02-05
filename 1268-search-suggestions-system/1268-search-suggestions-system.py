class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []

        prefix = ""
        left = 0

        for ch in searchWord:
            prefix += ch

            # Move left pointer to the first product >= prefix
            while left < len(products) and not products[left].startswith(prefix):
                left += 1

            suggestions = []
            # Collect up to 3 products starting with prefix
            for i in range(left, min(left + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])

            res.append(suggestions)

        return res
