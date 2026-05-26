class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)

        sorteds = sorted(slist)
        sortedt = sorted(tlist) #this will drive up the time comp

        if sorteds == sortedt:
            return True
        else:
            return False
        