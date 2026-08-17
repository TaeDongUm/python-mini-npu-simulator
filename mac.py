EPSILON = 1e-9


def calculate_mac(
    pattern: list[list[float]],
    filter_matrix: list[list[float]]
) -> float:
    score = 0.0
    size = len(pattern)

    for row in range(size):
        for col in range(size):
            score += pattern[row][col] * filter_matrix[row][col]

    return score


def determine_result(score_a: float, score_b: float) -> str:
    if abs(score_a - score_b) < EPSILON:
        return "UNDECIDED"

    if score_a > score_b:
        return "A"

    return "B"