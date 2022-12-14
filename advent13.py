import re

def toArray(msg):

    msg = msg[1:-1]
    array = []
    index = 0

    split = msg.split(',')

    for i in range(len(split)):

        if index >= len(split):
            break

        if len(split[index]) >= 2:
            begin = -1
            end = -1
            bracket = 0

            for i in range(len(msg)):
                if "[" == msg[i] and begin == -1:
                    begin = i

                if "[" == msg[i]:
                    bracket += 1

                if "]" == msg[i]:
                    bracket -= 1
                    if bracket == 0:
                        end = i
                        break

            # search = re.search("\[.*?\]", msg)
            subMsg = msg[begin: end+1]
            
            temp = toArray(subMsg)
            array.append(temp)

            index += len(temp)-1
            msg = msg[len(temp)*2+2:]
        else: 
            array.append(int(split[index]))

        index += 1

    return array

# while True:
# message1 = input()
# message2 = input()

msg1 = toArray("[1,[2,[3,[4,[5,6,0]]]],8,9]")
print(msg1)
# input()

