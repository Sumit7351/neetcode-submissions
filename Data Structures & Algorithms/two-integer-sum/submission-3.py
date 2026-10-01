class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,j in enumerate(nums):
            if target-j in map:
                return [map[target-j],map[j]]
            map[j]=i
        