from typing import List


def sum_numbers(nums: list[int]) -> int:
    """
    Takes a list of numbers and returns the result of:
    - Adding all positive numbers
    - Subtracting all negative numbers 

    Example:
        sum_numbers([2, -3, 5, -1]) → (2 + 5) - (3 + 1) = 3
    """
    # i = 0 
    # while i > 0:

    sum = 0
    subtract = 0
    
    for i in nums:
        if i >= 0:          
            sum = sum + i     
        elif i < 0:
            i = i * -1
            subtract = subtract + i
    return sum - subtract

# sum = 0
# for i in range(1, 4):
#     sum += i
# print(sum)

print(sum_numbers([2,-3,5,-1]))

def is_anagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams (ignoring case and spaces).
    
    Example:
        Input → str1 = "listen", str2 = "silent"
        Output → True
        
        Input → str1 = "hello", str2 = "world"
        Output → False
    """
    for i in str1.lower():
        if i in str2.lower():
            return True
        else:
            return False


def fibonacci_series(n_terms: int) -> List[int]:
    """
    Generate a Fibonacci series with n_terms.
    
    The series starts with 0, 1 and each subsequent term is the sum of the previous two.

    Example:
        Input → 10
        Output → [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    pass

def prime_factors(n: int) -> List[int]:
    """
    Return a list of all prime factors of a given number n.
    
    Example:
        Input → 84
        Output → [2, 2, 3, 7]
    """
    factors = []
    not_primes = []
    primes = []
    for i in range(1,n + 1):
        if n % i == 0:
            factors.append(i)
    for i in factors:
        for j in range(2, i):
            print(j)
            if i % j == 0:
                not_primes.append(j)
            else:
                primes.append(j)
    return primes
    # factors = []
    # prime = 2,3,5,7,11,13,17
    # for i in prime:
    #     if i % n == 0:           
    #     if int(n) // int(prime):
    #         return factors.append(i)

print(prime_factors(84))

def create_pyramid(n):
    """
    Returns a pyramid of '*' as a list of strings.

    Example:
        Input → 3
        Output →['  *  ', ' *** ', '*****']
    """
    pass

def create_number_triangle(n):
    """
    Returns a triangle of numbers as a list of strings.
    Example  :      
        Input → 3
        Output →    ['  1  ', ' 2 2 ', '3 3 3']
    """
    pass

def create_multiplication_square(n: int) -> List[str]:
    """
    Returns a multiplication square as a list of strings.
    Example:
        Input → 3
        Output → ['1 2 3', '2 4 6', '3 6 9']
    """
    user = int(input("Input a number :"))
    string = []


    for i in range(1,11):
        for n in range(i,user + 1):
            print(f"{i} {n} {i*n}")

        result = f"{i}{n}{i*n}"
        result = list(result)
        return result
               

# print(create_multiplication_square(3))


def create_diamond(n):
    """
    Returns a diamond shape as a list of strings.
    Example:
        Input → 3
        Output →    ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
    """    
    pass

def create_pascals_triangle(n: int) -> List[str]:
    """
    Return Pascal's triangle of height n as a list of strings.
        Example:
        Input → 5
        Output → ['    1    ', '   1 1   ',    '  1 2 1  ', ' 1 3 3 1 ', '1 4 6 4 1']
    """
    pass