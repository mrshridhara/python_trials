from typing import Text


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
