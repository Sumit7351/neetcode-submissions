class Solution:

    def encode(self, strs: List[str]) -> str:
        output=""
        n=0
        for s in strs:
            output+=s
            n+=1
            if n!=len(strs):
                output+="/"
        return output

    def decode(self, s: str) -> List[str]:
        res = s.split("/")
        return res

