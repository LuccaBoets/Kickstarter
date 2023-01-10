useCases = int(input())

for i in range(useCases):
    L, N = map(int, input().split(" "))
    
    pos = 0
    prevDir = 'C'
    finished = 0
    R = 0

    for j in range(N):
        D, Dir = input().split(" ")
        D = int(D)

        if Dir == 'C':
            R = (L - pos) % L
        else:
            R = pos

        if D < R:
            if Dir == 'C':
                pos += D
            else:
                pos -= D
        
        elif D >= R:
            if Dir == prevDir and R > 0:
                finished += 1

            finished += int((D-1-R)/L)

            if Dir == 'C':
                pos += (D-R)%L
            else:
                pos += L - ((D - R) % L)
            
            prevDir = Dir

    print(f"Case #{i+1}: {(finished)}")

    