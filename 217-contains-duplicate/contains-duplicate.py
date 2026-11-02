class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ans = {}
        for num in nums:
            if num in ans:
                return True
            ans[num] = ans.get(num, 0) + 1

        return False
