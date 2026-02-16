class Solution:
    def checkRecord(self, s: str) -> bool:
        eligibility = 1
        abscence_count = 0
        late_count = 0
        for day in s:
            if day=='L':
                late_count+=1
            else:
                late_count=0
            if day=='A':
                abscence_count+=1
            if late_count==3 or abscence_count>1:
                eligibility = 0
        return eligibility==1