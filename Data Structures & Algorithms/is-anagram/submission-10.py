class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)

        sorteds = sorted(slist)
        sortedt = sorted(tlist)

        if sorteds == sortedt:
            return True
        else:
            return False
        