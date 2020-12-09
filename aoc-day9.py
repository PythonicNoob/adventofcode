preamble = 25


def is_sum(data, number):
    sums = []
    for x in data:
        for y in data:
            sums.append(x+y)

    # print(data, number)

    if number in sums:
        return True
    return False

def main(preamble):
    data_stream = []
    with open("data.txt","r") as file:
        data_stream = [int(line.strip()) for line in file.readlines()]
    data_set = data_stream[:preamble]
    # print(data_set)
    for n in data_stream[preamble:]:
        if not is_sum(data_set, n):
            print("Number n is not matching", n)
            return

        del data_set[0]
        data_set.append(n)

# main(preamble)

def part2(number):
    with open("data.txt","r") as file:
        data = [int(line.strip()) for line in file.readlines()]
    for i in range(len(data)):
        sum = data[i]
        print(data[i],":")
        for x in range(i+1, len(data[i:])):
            print(data[x])
            sum += data[x]
            print(sum)

            if sum == number:
                rng = data[i:x+1]
                print(rng)
                print("Answer")
                print(max(rng))
                print(min(rng))
                print(max(rng)+min(rng))
                return


part2(36845998)
