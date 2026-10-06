class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(s.replace("/", "//") + "/#" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, cur, i = [], [], 0
        while i < len(s):
            if s[i] == "/":
                if s[i + 1] == "/":      # escaped literal slash
                    cur.append("/")
                else:                    # "/#" terminator
                    res.append("".join(cur))
                    cur = []
                i += 2
            else:
                cur.append(s[i])
                i += 1
        return res