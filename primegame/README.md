# Prime Game

Maria and Ben play a game using prime numbers.

## Function

isWinner(x, nums)

Returns the player who wins the most rounds.

## Algorithm

- Sieve of Eratosthenes to find prime numbers.
- Prefix sums to count primes efficiently.
- An odd number of primes means Maria wins.
- An even number of primes means Ben wins.

No external modules are imported.

Time complexity: O(N log log N + x)
Space complexity: O(N)
