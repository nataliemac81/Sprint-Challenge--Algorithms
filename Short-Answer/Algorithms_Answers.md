#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime of this snippet is O(n^3)
    
    a = 0 ---> O(1) constant
    while (a < n * n * n): ---> O(n^3)
      a = a + n * n ---> O(n^2)

      worst case scenario: 0(n^3)  


b) The run time for this snippet is O(n)

 sum = 0 ---> O(1)
    for i in range(n): ---> O(n)
      j = 1 ---> O(1)
      while j < n: ---> O(n)
        j *= 2 ---> O(1)
        sum += 1 --> O(1)

O(1) * O(n) ---> O(1 * n)
O(n) * O(1) ---> 0(n * 1)
O(1 * n) + O(n * 1) ----> O(2n * 1) ---> O(n * 1) ---> O(n)


c)

## Exercise II


