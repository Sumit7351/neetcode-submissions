class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        full_map=[]
        results=[]

        for word in strs:
            count={}
            for c in word:
                count[c]=count.get(c,0)+1
            full_map.append([count,True])

        for i in range(len(strs)):
            if full_map[i][1]==True:
                group=[strs[i]]
                for j in range(i+1,len(strs)):
                    if full_map[i][0]==full_map[j][0] and full_map[j][1]==True:
                        group.append(strs[j])
                        full_map[j][1]=False
                results.append(group)
            
        return results