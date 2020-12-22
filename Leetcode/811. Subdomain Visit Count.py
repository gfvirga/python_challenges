# 811. Subdomain Visit Count
# https://leetcode.com/problems/subdomain-visit-count/


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        log = {}
        for domain in cpdomains:
            times,name = domain.split(' ')
            
            sub_split = name.split('.')
            while len(sub_split) >= 1:
                sub = '.'.join(sub_split)
                if sub in log:
                    log[sub] += int(times)
                else:
                    log[sub] = int(times)
                sub_split.pop(0)
            
        return [str(v) + ' ' + k for k,v in log.items()]
            
        print(log)