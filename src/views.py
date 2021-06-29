from datetime import datetime

from flask import render_template

from . import app
from .domain.codekata import supermarket_pricing
from .domain.project_euler import (even_fibonacci_numbers,
                                   largest_palindrome_product,
                                   largest_prime_factor, multiples_of_3_and_5)
from .domain.types import ProblemGroup, ProblemStatement


problem_groups = {
    "project_euler":
    ProblemGroup("Project Euler")
        .append("multiples_of_3_and_5", ProblemStatement("Multiples of 3 and 5", multiples_of_3_and_5.__doc__))
        .append("even_fibonacci_numbers", ProblemStatement("Even Fibonacci Numbers", even_fibonacci_numbers.__doc__))
        .append("largest_prime_factor", ProblemStatement("Largest Prime Factor", largest_prime_factor.__doc__))
        .append("largest_palindrome_product", ProblemStatement("Largest Palindrome Product", largest_palindrome_product.__doc__)),
    "codekata":
    ProblemGroup("CodeKata")
        .append("supermarket_pricing", ProblemStatement("Supermarket Pricing", supermarket_pricing.__doc__)),
}


@app.route("/")
def home():
    return render_template(
        "problem_list.html",
        title="Problems List",
        current_year=datetime.now().year,
        problem_groups=problem_groups
    )


@app.route("/problems/<group_id>/<id>")
def problem_details(group_id, id):
    problem = problem_groups[group_id].problems[id]

    return render_template(
        "problem_details.html",
        title="Problem Details",
        current_year=datetime.now().year,
        problem=problem
    )
