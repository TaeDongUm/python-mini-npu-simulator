import time
from mac import calculate_mac

REPEAT_COUNT = 10

# MAC 연산을 여러 번 반복하고 평균 실행 시간을 ms 단위로 반환한다.
def measure_performance(
    pattern: list[list[float]],
    filter_matrix: list[list[float]]
) -> float:
    start = time.perf_counter()

    for _ in range(REPEAT_COUNT):
        calculate_mac(pattern, filter_matrix)

    end = time.perf_counter()

    total_time = end - start
    average_time = total_time / REPEAT_COUNT

    return average_time * 1000

# 성능 측정을 위해 지정한 크기의 N x N 테스트 행렬을 생성한다.
def create_test_matrix(size: int) -> list[list[float]]:
    matrix = []

    for _ in range(size):
        row = [1.0] * size
        matrix.append(row)

    return matrix

# 3x3, 5x5, 13x13, 25x25 크기의 MAC 성능을 측정한다.
def measure_sizes() -> list[tuple[int, float]]:
    sizes = [3, 5, 13, 25]
    results = []

    for size in sizes:
        pattern = create_test_matrix(size)
        filter_matrix = create_test_matrix(size)

        average_time = measure_performance(
            pattern,
            filter_matrix
        )

        results.append((size, average_time))

    return results