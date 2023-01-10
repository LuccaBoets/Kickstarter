from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentWater = 0

        validIndexes = []
        validHeights = []

        maxs = 0
        for i in range(len(heights)):
            if maxs <= heights[i]:
                validHeights.append(heights[i])
                validIndexes.append(i)
                maxs = heights[i]

        while True:
            offset = validIndexes[-1]+1
            subList = heights[offset:]
            if len(subList) == 0:
                break 
            
            maxIndex = 0
            maxs = 0
            for i in range(len(subList)):
                if maxs < subList[i]:
                    maxIndex = i
                    maxs = subList[i]

            validIndexes.append(maxIndex+offset)
            validHeights.append(maxs)

        left = 0
        right = len(validHeights)-1
        currentWater = self.reqursief(0, left, right, validIndexes, validHeights)

        # for i in range(len(validHeights)):
        #     currentHeight = validHeights[i]          
        #     for j in range(len(validHeights)):
        #         selectedHeight = validHeights[j]

        #         if currentHeight <= selectedHeight:
        #             distance = abs(validIndexes[i]-validIndexes[j])
                    
        #             calcWater = distance * currentHeight
                    
        #             if calcWater > currentWater:
        #                 currentWater = calcWater

        return currentWater

    def reqursief(self, currentWater, left, right, validIndexes, validHeights):

        if right == 0 or left == len(validIndexes):
            return currentWater

        distance = abs(validIndexes[left]-validIndexes[right])
        
        currentHeight = min(validHeights[left], validHeights[right])

        calcWater = distance * currentHeight

        print(calcWater)
        print(left)
        print(right)
        print()
        

        
        if calcWater >= currentWater:
            currentWater = calcWater

            if validHeights[left] == validHeights[right]:
                return self.reqursief(currentWater, left+1, right-1, validIndexes, validHeights)
            elif currentHeight == validHeights[left]:
                return self.reqursief(currentWater, left+1, right, validIndexes, validHeights)

            elif currentHeight == validHeights[right]:
                return self.reqursief(currentWater, left, right-1, validIndexes, validHeights)

        return currentWater


        
solution = Solution()

print(solution.maxArea([2,3,4,5,18,17,6]))