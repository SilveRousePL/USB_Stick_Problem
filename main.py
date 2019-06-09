# Args:   integer number which will be transformed, length
# Return: Tuple(binary number) (0,1,1,0,0,...)
def generate_solution(number, size):
    a = [int(x) for x in bin(number)[2:]]
    b = [0] * (size-len(a))
    return tuple(b+a)

# Bruteforce:
# Args:   capacity, List[Tuple(name, weight, price)]
# Return: Tuple(price_summary, {name1, name2, ...})
def knapsack_BF(capacity, objects):
    best_price_summary = 0
    solution = []
    for i in range(0, 2**len(objects)):
        binary_solution = generate_solution(i, len(objects))
        weight_summary = 0
        price_summary = 0
        for j in range(0, len(binary_solution)):
            if binary_solution[j] is 1:
                weight_summary += objects[j][1]
                price_summary += objects[j][2]
        if weight_summary > capacity:
            continue
        if price_summary > best_price_summary:
            best_price_summary = price_summary
            solution.clear()
            for j in range(0, len(binary_solution)):
                if binary_solution[j] is 1:
                    solution.append(objects[j][0])
    return (best_price_summary, set(solution))


# Dynamic programming:
# Args:   capacity, List[Tuple(name, weight, price)], len(List)
# Return: (price_summary, {name1, name2, ...})
def knapsack_DP(capacity, objects):
    K = [[0 for x in range(capacity + 1)] for x in range(len(objects) + 1)]
    L = [[ [] for x in range(capacity + 1)] for x in range(len(objects) + 1) ]
    for i in range(len(objects) + 1):
        for j in range(capacity + 1):
            if i is 0 or j is 0:
                K[i][j] = 0
                L[i][j].clear()
            elif objects[i-1][1] <= j:
                if K[i-1][j] > objects[i-1][2] + K[i-1][j-objects[i-1][1]]:
                    K[i][j] = K[i-1][j]
                    L[i][j] = L[i-1][j]
                else:
                    K[i][j] = objects[i-1][2] + K[i-1][j-objects[i-1][1]]
                    L[i][j].clear()
                    for elem in L[i-1][j-objects[i-1][1]]:
                        L[i][j].append(elem)
                    L[i][j].append(objects[i-1][0])
            else:
                K[i][j] = K[i-1][j]
                L[i][j] = L[i-1][j]
    return (K[len(objects)][capacity], set(L[len(objects)][capacity]))


# Args:   int(Capacity[GiB]), List[Tuple(str(Name), int(Size[MiB]), int(Price))]
# Return: (price_summary, {'name1', 'name2' , ...})
def calculate(usb_size, memes):
    usb_size *= 1024
    DP_complexity = usb_size*len(memes)
    BF_complexity = 2**len(memes)
    if DP_complexity < BF_complexity:
        result = knapsack_DP(usb_size, memes)
    else:
        result = knapsack_BF(usb_size, memes)
    return result