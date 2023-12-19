class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result ={}
        res=[]
        for domains in cpdomains:
            num, dom = domains.split(" ")
            dom_list = dom.split(".")
            for i in range(len(dom_list)):
                result['.'.join(dom_list[i:])] = result.get('.'.join(dom_list[i:]),0)+int(num)
        for key , value in result.items():
            s = ""
            s = str(value) + " " + key
            res.append(s)
        return res