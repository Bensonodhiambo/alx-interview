For this problem, you need to calculate the fewest number of operations (Copy All and Paste) to achieve exactly n characters of "H" in a text file. Here's how to approach it, step by step:

Key Insight: Prime Factorization
The problem can be reduced to prime factorization because, for any given number n, the number of operations is closely related to the sum of the prime factors of n. This is because the most efficient way to generate n characters is by copying and pasting sequences of characters in batches that are divisible by prime numbers.

Algorithm Outline:
Prime Factorization: For a given number n, break it down into its prime factors.
Sum of Factors: The minimum number of operations will be the sum of these factors. This is because to reach n, you need to "build up" by duplicating the largest possible factor at each step.
Steps:
Start with 1 "H".
Factorize n to get its prime factors.
For each factor, you'll perform a "Copy All" operation, followed by a series of "Paste" operations based on the size of the factor.
Example for n = 9:
Prime factors of 9 are: 3, 3.
Operations:
Start with H.
Copy All, Paste (3 H's) → 3 operations.
Copy All, Paste (9 H's) → 3 more operations.
Total: 6 operations.
