import math
import random
import time

def calc_price(solution, objects):
    price_summary = 0
    for i in range(0, len(solution)):
        if solution[i] is 1:
            price_summary += objects[i][2]
    return price_summary

def calc_weight(solution, objects):
    weight_summary = 0
    for i in range(0, len(solution)):
        if solution[i] is 1:
            weight_summary += objects[i][1]
    return weight_summary

def generate_adjacent_solution(solution):
    solution = list(solution)
    x1 = random.randint(0, len(solution) - 1)
    if solution[x1] is 1:
        solution[x1] = 0
    else:
        solution[x1] = 1
    solution = tuple(solution)
    return solution

def generate_solution(number, size):
    a = [int(x) for x in bin(number)[2:]]
    b = [0] * (size-len(a))
    return tuple(b+a)

def generate_solution_greedy(capacity, objects):
    solution = []
    objects = list(objects)
    for i in range(0, len(objects)):
        if capacity - objects[i][1] >= 0:
            solution.append(1)
            capacity -= objects[i][1]
            if capacity is 0:
                break
        else:
            solution.append(0)
    return tuple(solution)


# Approximately O(n^4)
# Args:   capacity, List[Tuple(name, weight, price)]
# Return: price_summary, {name1, name2, ...}
def knapsack_SA(capacity, objects):
    worse_solution_counter = 0
    worse_acceptable = 5 * len(objects)
    temperature = 1000
    temperature_change_factor = 0.99
    current_solution = generate_solution(random.randint(1, 2**len(objects)) - 1, len(objects))
    while calc_weight(current_solution, objects) > capacity:
        current_solution = generate_solution(random.randint(1, 2**len(objects)) - 1, len(objects))
    #current_solution = generate_solution_greedy(capacity, objects)
    print("Greedy:", calc_price(current_solution, objects))
    best_solution = current_solution
    adjacent_solution = current_solution
    price_current_solution = calc_price(current_solution, objects)
    price_best_solution = price_current_solution
    price_adjacent_solution = 0

    while worse_solution_counter < worse_acceptable:
        adjacent_solution = generate_adjacent_solution(current_solution)
        if calc_weight(adjacent_solution, objects) > capacity:
            adjacent_solution = list(adjacent_solution)
            for i in range(0, len(adjacent_solution)):
                if adjacent_solution[i] is 1:
                    adjacent_solution[i] = 0
                    adjacent_solution = tuple(adjacent_solution)
                    break
            continue
        price_adjacent_solution = calc_price(adjacent_solution, objects)

        if price_adjacent_solution > price_best_solution:
            best_solution = adjacent_solution
            price_best_solution = price_adjacent_solution

        if price_adjacent_solution > price_current_solution:
            current_solution = adjacent_solution
            price_current_solution = price_adjacent_solution
            worse_solution_counter = 0
        else:
            worse_solution_counter += 1
            delta = price_current_solution - price_adjacent_solution
            x = random.random()
            if x < (math.exp(-delta / temperature)):
                current_solution = adjacent_solution
                price_current_solution = price_adjacent_solution

        temperature *= temperature_change_factor
    solution = []
    for i in range(0, len(best_solution)):
        if best_solution[i] is 1:
            solution.append(objects[i][0])
    return (price_best_solution, set(solution))

# Args:   int(Capacity[GiB]), List[Tuple(str(Name), int(Size[MiB]), int(Price))]
# Return: (price_summary, {'name1', 'name2' , ...})
def calculate(usb_size, memes):
    usb_size *= 1024
    usb_size = int(usb_size)
    timer = time.perf_counter_ns()
    result = knapsack_SA(usb_size, memes)
    timer = time.perf_counter_ns() - timer
    print("Wynik:", result)
    print("Czas:", timer/1000000, "ms")
    return result

with open('zestaw2') as file:
    capacity = int(file.readline())
    memes = []
    for line in file:
        meme = line.split()
        meme[1] = int(meme[1])
        meme[2] = int(meme[2])
        meme = tuple(meme)
        memes.append(meme)

print(calculate(capacity, memes))