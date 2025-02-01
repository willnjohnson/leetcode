class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort citations in descending order
        citations.sort(reverse=True)
        
        # Traverse the sorted list to find the h-index
        for i in range(len(citations)):
            # If number of citations at index i is less than or equal to i, we found the h-index
            if citations[i] < i + 1:
                return i
        
        # All papers have more than i citations, so h-index is the total number of papers
        return len(citations)
