from constraint import Problem, AllDifferentConstraint

def n_queens_solver(n):
    problem = Problem()
    cols = range(n)
    rows = range(n)

    # Add variables to the problem
    problem.addVariables(cols, rows)

    # Add constraints
    problem.addConstraint(AllDifferentConstraint())

    # Add diagonal constraints
    for col1 in cols:
        for col2 in cols:
            if col1 < col2:
                problem.addConstraint(lambda row1, row2, col1=col1, col2=col2: abs(row1 - row2) != abs(col1 - col2), (col1, col2))

    # Solve the problem
    solutions = problem.getSolutions()
    return solutions


# Example usage
solutions = n_queens_solver(4)
for solution in solutions:
    for col, row in solution.items():
        print(f"Queen at column {col} and row {row}")
    print()
