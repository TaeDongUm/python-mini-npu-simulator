from matrix import input_matrix
from mac import calculate_mac, determine_result
from performance import measure_performance
from analyzer import load_data, select_filters


def select_mode() -> str:
    print("=== Mini NPU Simulator ===")
    print()
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")

    mode = input("선택: ").strip()

    return mode


def main() -> None:
    mode = select_mode()

    if mode == "1":
        filter_a = input_matrix("필터 A")
        filter_b = input_matrix("필터 B")
        pattern = input_matrix("패턴")

        score_a = calculate_mac(pattern, filter_a)
        score_b = calculate_mac(pattern, filter_b)

        result = determine_result(score_a, score_b)

        average_time = measure_performance(
            pattern,
            filter_a
        )

        print(f"\nA 점수: {score_a}")
        print(f"B 점수: {score_b}")
        print(f"연산 시간(평균/10회): {average_time:.6f} ms")

        if result == "UNDECIDED":
            print("판정: 판정 불가")
        else:
            print(f"판정: {result}")

    if mode == "2":
        filters, patterns = load_data("data.json")

        for case_id in patterns:
            selected_filters = select_filters(case_id, filters)
            print(f"{case_id} -> 필터 선택 완료")

        print("filters 로드 완료")
        print("patterns 로드 완료")


if __name__ == "__main__":
    main()