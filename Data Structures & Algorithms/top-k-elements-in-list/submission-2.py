class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        arr=[]
        for n in nums:
            count[n]=count.get(n,0)+1

        arr=sorted(count.items(),key=lambda n:n[1],reverse=True)

        result=[]
        for n in range(0,k):
            result.append(n[0])

        return result