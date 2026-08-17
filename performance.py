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