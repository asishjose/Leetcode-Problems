class Solution:
    def checkRecord(self, s: str) -> bool:
        eligibility = 1
        if s.count('A')>1:
            eligibility = 0
        late_count = 0
        for day in s:
            if day=='L':
                late_count+=1
            else:
                late_count=0
            if late_count==3:
                eligibility = 0
        if eligibility==1:
            return True
        else:
            return False
