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