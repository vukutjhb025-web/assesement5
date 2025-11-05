from typing import List


def sum_numbers(nums: list[int]) -> int:
    """
    Takes a list of numbers and returns the result of:
    - Adding all positive numbers
    - Subtracting all negative numbers 

    Example:
        sum_numbers([2, -3, 5, -1]) → (2 + 5) - (3 + 1) = 3
    """
    pass

def is_anagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams (ignoring case and spaces).
    
    Example:
        Input → str1 = "listen", str2 = "silent"
        Output → True
        
        Input → str1 = "hello", str2 = "world"
        Output → False
    """
    pass

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
    pass

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
    pass


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