class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]

        for i in range(len(nums)):
            l=0
            r=i+1
            leftP=rightP=1
            while(l!=i):
                leftP*=nums[l]
                l+=1
            while(r<len(nums)):
                rightP*=nums[r]
                r+=1
            result.append(leftP*rightP)

        return result