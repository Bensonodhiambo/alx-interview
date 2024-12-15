"""
Prime Game Package

This package provides tools to determine the winner of a competitive game 
involving prime numbers. It includes functionalities to:
    - Identify prime numbers efficiently using the Sieve of Eratosthenes.
    - Compute cumulative prime counts for game rounds.
    - Determine the winner across multiple rounds.

Modules:
    - prime_game: Contains the core logic for the prime game.

Usage:
    from prime_game import isWinner

    winner = isWinner(3, [4, 5, 1])
    print(winner)  # Outputs: 'Ben'
"""
