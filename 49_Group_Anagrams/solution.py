class Solution:
    def groupAnagrams(self, strs):
        res = {}

        for s in strs:
            # Create count of characters ('a' to 'z')
            cnt = [0] * 26

            for char in s:
                cnt[ord(char) - ord('a')] += 1

            key = tuple(cnt)  # Use tuple of counts as key

            if key in res:  res[key].append(s)
            else:           res[key] = [s]

        return list(res.values())
