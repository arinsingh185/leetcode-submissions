class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ans = {}
        for num in nums:
            ans[num] = ans.get(num, 0) + 1

        for num in nums:
            if ans[num] > 1:
                return True

        return False
