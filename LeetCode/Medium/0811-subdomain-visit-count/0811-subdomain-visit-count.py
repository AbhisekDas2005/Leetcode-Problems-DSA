class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        f = {}
        for i in cpdomains:
            space=i.find(" ")
            n=int(i[:space])
            ls=i[space + 1:].split(".")
            for j in range(len(ls)):
                domain = ".".join(ls[j:])
                if domain in f:
                    f[domain]+=n
                else:
                    f[domain]=n
        l=[]
        for i in f:
            n=f[i]
            na=i
            l.append(str(n)+" "+na)
        return l
            
            

            