from matrix import input_matrix
from mac import calculate_mac, determine_result
from performance import measure_performance
from analyzer import (
    load_data,
    extract_size,
    select_filters,
    normalize_label,
)
from matrix import validate_matrix
from performance import measure_performance, measure_sizes


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

        total_count = 0
        pass_count = 0
        fail_count = 0
        failures = []

        for case_id, case_data in patterns.items():
            total_count += 1
            try:
                size = extract_size(case_id)
                selected_filters = select_filters(case_id, filters)

                pattern = case_data["input"]

                if not validate_matrix(pattern, size):
                    print(f"{case_id}: 패턴 크기 오류 - 다음 케이스로 이동")
                    continue
                cross_filter = None
                x_filter = None

                for filter_name, filter_matrix in selected_filters.items():
                    label = normalize_label(filter_name)

                    if label == "Cross":
                        cross_filter = filter_matrix

                    if label == "X":
                        x_filter = filter_matrix

                if cross_filter is None or x_filter is None:
                    print(f"{case_id}: 필요한 필터가 없습니다.")
                    continue

                if not validate_matrix(cross_filter, size):
                    print(f"{case_id}: Cross 필터 크기 오류")
                    continue

                if not validate_matrix(x_filter, size):
                    print(f"{case_id}: X 필터 크기 오류")
                    continue

                cross_score = calculate_mac(pattern, cross_filter)
                x_score = calculate_mac(pattern, x_filter)

                result = determine_result(
                    cross_filter,
                    x_score,
                    "Cross",
                    "X"
                )

                expected = normalize_label(case_data["expected"])

                if expected is None:
                    print(f"{case_id}: expected 라벨 오류")
                    continue
                if result == expected:
                    status = "PASS"
                    pass_count += 1
                else:
                    status = "FAIL"
                    fail_count += 1

                if status == "FAIL":
                    if result == "UNDECIDED":
                        reason = "epsilon 기준 동점으로 UNDECIDED 판정"
                    else:
                        reason = f"expected={expected}, prediction={result}"
                    failures.append(
                        {
                            "case_id": case_id,
                            "reason" : reason,
                        }
                    )

                performance_results = measure_sizes()

                print(f"\n--- {case_id} ---")
                print(f"Cross 점수: {cross_score}")
                print(f"X 점수: {x_score}")
                print(f"판정: {result}")
                print(f"expected: {expected}")
                print(f"결과: {status}")

                print("\n#---------------------------------------")
                print("# 성능 분석")
                print("#---------------------------------------")

                print(f"{'크기':<10}{'평균 시간(ms)':<20}{'연산 횟수'}")
                print("-" * 45)

                for size, average_time in performance_results:
                    operation_count = size * size

                    print(
                        f"{size}x{size:<7}"
                        f"{average_time:<20.6f}"
                        f"{operation_count}"
                    )

            except (KeyError, ValueError, TypeError) as error:
                print(f"{case_id}: 데이터 오류 ({error}) - 다음 케이스로 이동")
                continue

        print("\n#---------------------------------------")
        print("# 결과 요약")
        print("#---------------------------------------")

        print(f"총 테스트: {total_count}개")
        print(f"통과: {pass_count}개")
        print(f"실패: {fail_count}개")

        # print("filters 로드 완료")
        # print("patterns 로드 완료")


if __name__ == "__main__":
    main()