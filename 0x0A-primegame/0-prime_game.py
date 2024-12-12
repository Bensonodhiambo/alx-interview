#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """
    Generate a list of booleans where True indicates that the index is a prime number.
    """
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    return is_prime

def calculate_prime_counts(is_prime):
    """
    Precompute the cumulative count of prime numbers up to each index.
    """
    prime_count = [0] * len(is_prime)
    for i in range(1, len(is_prime)):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)
    return prime_count

def isWinner(x, nums):
    """
    Determine the winner of the prime game.
    Args:
        x: Number of rounds.
        nums: List of integers, where each represents the maximum number in a round.
    Returns:
        Name of the player with the most wins ("Maria" or "Ben"), or None if tied.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)
    prime_count = calculate_prime_counts(is_prime)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))

