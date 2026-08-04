class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            pre = str(len(i))
            encode += pre+"#"+i
        return encode

    def decode(self, s: str) -> List[str]:
        decode  = []
        i = 0
        print(s)
        while s:
            rng = s.split("#")[0]
            j = len(rng)
            decode.append(s[j+1:j+1+int(rng)])
            s = s[j+1+int(rng):]
            print(s)
        return decode

