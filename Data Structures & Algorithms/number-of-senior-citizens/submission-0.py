class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            if len(details[i])>15:
                continue

            if details[i][10] != 'M' and details[i][10] != 'F' and details[i][10] != 'O':
                continue

            age = int(details[i][11] + details[i][12])
            if age > 60:
                count = count + 1 
            else:
                continue
            
        return count