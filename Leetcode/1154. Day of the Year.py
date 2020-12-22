# 1154. Day of the Year
# https://leetcode.com/problems/day-of-the-year/

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split('-')
        
        days = 0
        
        months = {
            1: 31,
            2: 29 if int(year)%4 == 0 and int(year) != 1900 else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
            
        }
        
        print(months)
        for m in range(1, int(month)):        
            days += months[m]
            
        days += int(day)
        
        return days