"""
Prime Game Module

This module implements a competitive game played by two players, Maria and Ben. The game involves 
choosing prime numbers and their multiples from a set of integers. The players take turns, 
starting with Maria, and play optimally. The player who cannot make a move loses the game.

Key Features:
    - Efficient identification of prime numbers using the Sieve of Eratosthenes algorithm.
    - Precomputing cumulative prime counts for fast evaluation during gameplay.
    - Determination of the winner based on the rules of the game across multiple rounds.

Functions:
    sieve_of_eratosthenes(max_n): 
        Identifies all prime numbers up to a given number `max_n` using the Sieve of Eratosthenes.

    calculate_prime_counts(is_prime): 
        Computes cumulative prime counts for quick reference during game rounds.

    isWinner(x, nums): 
        Determines the overall winner of the game after multiple rounds by evaluating optimal gameplay.

Usage Example:
    >>> print(isWinner(3, [4, 5, 1]))
    'Ben'

Author:
    Benson Odhiambo

Date:
    2024-12-14
"""

