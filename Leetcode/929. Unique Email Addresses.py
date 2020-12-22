# 929. Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            name, domain = email.split("@")
            name = name.split("+")[0]
            name = ''.join(e for e in name if e.isalnum())
            name = name + "@" + domain
            res.add(name)
            
        print(res)
        return len(res)