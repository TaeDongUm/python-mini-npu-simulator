def input_matrix(title: str, size: int = 3) -> list[list[float]]:
    print(f"\n{title} ({size}줄 입력, 공백 구분)")

    matrix = []

    for _ in range(size):
        row = list(map(float, input().split()))
        matrix.append(row)

    return matrix