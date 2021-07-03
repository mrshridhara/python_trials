"""
Defines the domain types useful in discovring and registering problems.
"""

from .codekata import supermarket_pricing
from .project_euler import (even_fibonacci_numbers, largest_palindrome_product,
                            largest_prime_factor, multiples_of_3_and_5)


class ProblemGroup:
    def __init__(self, name):
        self.name = name
        self.problems = {}

    def append(self, id, problem):
        self.problems[id] = problem
        return self


class ProblemStatement:
    def __init__(self, name, description):
        self.name = name
        self.description = description


problem_groups = {
    "project_euler":
        ProblemGroup("Project Euler")
            .append(
                "multiples_of_3_and_5",
                ProblemStatement("Multiples of 3 and 5", multiples_of_3_and_5.__doc__)
            )
            .append(
                "even_fibonacci_numbers",
                ProblemStatement("Even Fibonacci Numbers", even_fibonacci_numbers.__doc__)
            )
            .append(
                "largest_prime_factor",
                ProblemStatement("Largest Prime Factor", largest_prime_factor.__doc__)
            )
            .append(
                "largest_palindrome_product",
                ProblemStatement("Largest Palindrome Product", largest_palindrome_product.__doc__)
            ),

    "codekata":
        ProblemGroup("CodeKata")
            .append(
                "supermarket_pricing",
                ProblemStatement("Supermarket Pricing", supermarket_pricing.__doc__)
            ),
}
