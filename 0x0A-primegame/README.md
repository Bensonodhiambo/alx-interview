Explanation of the Code
Sieve of Eratosthenes:

Used to generate a boolean list (is_prime) indicating whether each number up to max_n is prime.
Prime Counts:

A cumulative count of primes up to each index is precomputed using calculate_prime_counts.
Game Logic:

For each round:
Count the number of primes up to n using the prime_count array.
If the count is odd, Maria wins the round; otherwise, Ben wins.
Determine Winner:

Compare the total wins for Maria and Ben to determine the overall winner.
