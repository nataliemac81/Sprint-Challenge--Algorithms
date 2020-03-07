#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime of this snippet is O(n^3)
    
    a = 0 ---> O(1) constant
    while (a < n * n * n): ---> O(n^3)
      a = a + n * n ---> O(n^2)

      worst case scenario: 0(n^3)  


b) The runtime for this snippet is O(n)

 sum = 0 ---> O(1)
    for i in range(n): ---> O(n)
      j = 1 ---> O(1)
      while j < n: ---> O(n)
        j *= 2 ---> O(1)
        sum += 1 --> O(1)

O(1) * O(n) ---> O(1 * n)
O(n) * O(1) ---> 0(n * 1)
O(1 * n) + O(n * 1) ----> O(2n * 1) ---> O(n * 1) ---> O(n)


c) The runtime for this snippet is O(n)

def bunnyEars(bunnies): ---> function will be called n (or bunnies) times 
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) ---> for each function call, add 2 ---> 0(1)

number of function calls (n) * work done in each call (O(1)) ---> O(n)

## Exercise II

def drop_eggs(building):
    safe_floors = []
    floor_start_breaking_eggs = (len(building) / 2)

    for floor in range(0, len(building))
        if floor >= floor_start_breaking_eggs:
            break eggs
        else:
            safe_floors.append(floor)

        return safe_floors



