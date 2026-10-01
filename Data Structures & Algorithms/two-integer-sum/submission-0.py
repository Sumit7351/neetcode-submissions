class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,j in enumerate(nums):
            map[j]=i

        for n in map:
            if target-n in map:
                return [map[n],map[target-n]]
        