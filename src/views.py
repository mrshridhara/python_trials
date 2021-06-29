from datetime import datetime

from flask import render_template

from . import app
from .domain.types import problem_groups


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
