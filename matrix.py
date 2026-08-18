def input_matrix(title: str, size: int = 3) -> list[list[float]]:
    print(f"\n{title} ({size}줄 입력, 공백 구분)")

    matrix = []

    while len(matrix) < size:
        try:
            row = list(map(float, input().split()))
        except ValueError:
            print("입력 형식 오류: 숫자만 입력하세요.")
            continue

        if len(row) != size:
            print(
                f"입력 형식 오류: 각 줄에 {size}개의 숫자를 "
                "공백으로 구분해 입력하세요."
            )
            continue

        matrix.append(row)

    return matrix

# 행렬이 정확한 N x N 크기인지 검증한다.
def validate_matrix(
    matrix: list[list[float]],
    size: int
) -> bool:
    if len(matrix) != size:
        return False

    for row in matrix:
        if len(row) != size:
            return False

    return True