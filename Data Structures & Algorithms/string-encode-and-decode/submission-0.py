class Solution:

    def encode(self, strs: List[str]) -> str:
        output=""
        for s in strs:
            output+=s
            output+=" "
        return output

    def decode(self, s: str) -> List[str]:
        res = s.split()
        return res

