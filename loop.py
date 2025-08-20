from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # urutkan dari terbesar
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        return h
