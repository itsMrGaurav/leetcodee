class Solution:
    def intervalIntersection(self, firstList: list, secondList: list) -> list:

        # basecases
        if firstList == [] or secondList == []: return []


        res = []
        i,j = 0,0
        while i < len(firstList) and j < len(secondList):
            s1, s2 = firstList[i][0], secondList[j][0]
            e1, e2 = firstList[i][1], secondList[j][1]
            if s1 > e2 or s2 > e1:
                if s1 > e2 : j += 1
                else: i += 1
                continue 
            if e1 > e2:         # [1,4], [2, 3]
                if s1 < s2:
                    res.append([s2,e2])
                else:
                    res.append([s1,e2])
                j+=1
            else:
                if s1 > s2:
                    res.append([s1,e1])
                else:
                    res.append([s2,e1])
                i+=1
        return res


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
s = Solution()
print(s.intervalIntersection(firstList, secondList))