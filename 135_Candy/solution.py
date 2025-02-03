class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        # O(n) time complexity - only go through list twice (once left and once right)
        # O(n) space complexity - candies array is same size as ratings array

        # Initialize candies array where every child gets at least 1 candy
        candies = [1] * n

        # Perform left to right pass
        # If a child has a higher rating than the one before it, they get more candy than that child
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Perform right to left pass
        # If a child has a higher rating than the one after it, they get more candy than that child
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Return total number of candies
        return sum(candies)
