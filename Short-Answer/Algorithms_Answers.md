#### Please add your answers to the ***Analysis of Algorithms*** exercises here.

## Exercise I

a) Here, the runtime is O(n). The while loop contains n^3, but in each pass of the loop, we are adding n^2, so we must add n^2 n times to reach n^3. Thus, the loop will run n times, hence O(n).


b) Here, the runtime is O(n log n). The outer for loop will run n times, and the inner for loop will run log_2 (n) times for each time the outer loop runs.


c) Here, the runtime is O(n) if n > 0 and infinite recursion if n < 0. The function will run n times where n = # of bunnies, and never reach the base case if n < 0.

## Exercise II

If we have an infinite supply of eggs, then a binary search for the floor f would be the most efficient since we will always have a worst case scenario of broken + dropped eggs = log_2(n). If we are only checking log_2(n) floors for when the egg breaks, then this algorithm has runtime complexity O(log n). 

Pseudocode for the binary search is as follows:

```
if n is 0: return 0

if n is 1: return 1

else:
    the lowest floor = 1
    the highest floor = n
    
    while highest and lowest floors are at least 1 apart:
        the middle floor = lowest floor + (midpoint of distance between lowest and highest floors)
        drop the egg
        if egg breaks:
            set highest floor = middle
        else:
            set lowest floor = middle
    
    drop the egg for the last time
    if egg breaks:
        floor f is lowest - 1
    if not:
        floor f is lowest
    
```
