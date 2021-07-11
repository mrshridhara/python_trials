from flask import render_template

from . import app, current_year
from .types import problem_groups


@app.route("/")
def home():
    return render_template(
        "problem_list.html",
        title="Problems List",
        current_year=current_year,
        problem_groups=problem_groups
    )


@app.route("/<group_id>/<id>")
def problem_details(group_id, id):
    problem_group = problem_groups.get(group_id)
    if (problem_group is None):
        return render_template(
            "status_code_404.html",
            title="Not Found",
            current_year=current_year
        ), 404

    problem = problem_group.problems.get(id)
    if (problem is None):
        return render_template(
            "status_code_404.html",
            title="Not Found",
            current_year=current_year
        ), 404

    return render_template(
        "problem_details.html",
        title=f"{problem.name} | {problem_group.name}",
        current_year=current_year,
        problem=problem
    )
