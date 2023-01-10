useCases = int(input())

for i in range(useCases):
    totalDistance, runCount = map(int, input().split(" "))
    
    currentDistance = 0
    lastDirection = 'C'
    finished = 0

    for j in range(runCount):
        distance, direction = input().split(" ")
        distance = int(distance)

        finishedTemp = 0

        if direction == 'C':
            currentDistance += distance
        else:
            currentDistance -= distance

        crossed = False

        if direction == 'C':
            finishedTemp += int(currentDistance / totalDistance)

        elif direction == 'A':
            finishedTemp += int(abs(currentDistance / totalDistance))
            if currentDistance < 0:
                finishedTemp += 1

        if finishedTemp > 0:
            crossed = True

        if direction != lastDirection and crossed:
            finishedTemp -= 1

        finished += finishedTemp

        if crossed:
            lastDirection = direction
        currentDistance = (currentDistance % totalDistance)

        # if currentDistance == 0:
        #     lastDirection = direction

        # while index != 0:
        #     index -= 1

        #     if direction == 'C':
        #         currentDistance += 1
        #     else:
        #         if currentDistance == 0:
        #             currentDistance = totalDistance
        #         currentDistance -= 1

        #     currentDistance = abs(currentDistance)

        #     if (currentDistance == 0 or currentDistance == totalDistance):
        #         if lastDirection == direction:
        #             finished += 1

        #         lastDirection = direction
        #         currentDistance %= totalDistance

        # ----

        # if direction == 'C':
        #     currentDistance += distance
        # else:
        #     currentDistance -= distance

        # currentDistance = currentDistance

        # # if currentDistance >= :

        # if (currentDistance <= 0 or currentDistance >= totalDistance):

        #     if currentDistance >= totalDistance*2:
        #         finished += int(currentDistance/totalDistance)-1
        #         currentDistance = (currentDistance % totalDistance)

        #     elif currentDistance <= -totalDistance*2:
        #         finished += int(abs(currentDistance)/totalDistance)-1
        #         currentDistance = (currentDistance % totalDistance)

        #     if lastDirection == direction:
        #         finished += 1
        #         currentDistance = (currentDistance % totalDistance)

        #     lastDirection = direction


        # print(f"currentDistance: {currentDistance}")
        # print(f"finished: {finished}")
        # print(f"lastDirection: {lastDirection}")

    print(f"Case #{i+1}: {int(finished)}")
