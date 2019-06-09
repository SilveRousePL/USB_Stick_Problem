# USB Stick Problem
## Based on knapsack problem
### Python Clearcode intern summer 2019 task
---

## Task (tl;dr)
Need to be write function `calculate(usb_size, memes)` that calculates the best set of memes, so that he can sell the USB stick for the highest price.
- `usb_size: int` -
a number describing the capacity of the USB stick in GiB - e.g. 1 ​ means a USB with 1 GiB capacity.
- ` memes: List[Tuple[str, int, int]]` - is a list of 3-element tuples, each with the name, size in MiB, and price in caps of a
meme.

The function should return a tuple with the first element being the total value of all memes on
the USB stick, and the second being the set of names of the memes that should be copied
onto the USB stick to maximize its value.

## `Calculate` Function description
`usb_size` variable is multiplied by 1024 (GiB -> MiB) and then calculation complexity is calculated in order to select the better algorithm. The algorithms used in this task are Bruteforce and Dynamic Programming. 

The function return `Tuple(price_summary, {name1, name2, ...})`.

## `Generate solution` function description

- `number: int` - integer number which will be transformed to a binary.
- `size: int` - length of return tuple.

The function return tuple of binary representation of number given in argument and the tuple has length given in the second argument (the function adds zero at the beginning of the tuple to extend).

## Bruteforce algorithm
Args:
- `capacity: int`
- `memes: List[Tuple(name, weight, price)]`

Algorithm calculate the best solution by checking all possible solutions. The solution is generated with an auxiliary function `generate_solution(number, size)`.

The solutions are generated in sequence and each is checked whether the weight does not exceed the capacity and whether the price is higher than in the previous best solution. This algorithm has complexity `O(2^n)`.

The function return `Tuple(price_summary, {name1, name2, ...})`.

## Dynamic programming
Args:
- `capacity: int`
- `memes: List[Tuple(name, weight, price)]`

In the algorithm, computed solutions to subproblems are stored in a table so that these don’t have to be recomputed. The knapsack problem has optimal substructure property and overlapping subproblems property. So, I use tabulation (Bottom Up) to avoid generating overlapping subproblems. Due to this algorithm has complexity `O(capacity*n)`.

The function return `Tuple(price_summary, {name1, name2, ...})`.

## Summary
In the meantime, I tried to create an algorithm of Simulated Annealing (metaheuristics) to solve very big problems, but there is a small bug in it, which manifests itself in some test cases. I will certainly improve it later. Due to this task I have learned new things :)

![](http://www.netimperative.com/wp-content/uploads/2015/12/pepe-the-frog.jpg)
