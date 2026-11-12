class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Initialize a boolean list where True means prime
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # Apply the Sieve of Eratosthenes
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i starting from i*i as False
                for j in range(i * i, n, i):
                    is_prime[j] = False
                    
        # Return the count of True values in is_prime
        return sum(is_prime)
