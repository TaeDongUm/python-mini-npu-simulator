from matrix import input_matrix
from mac import calculate_mac, determine_result


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

        print(f"\nA 점수: {score_a}")
        print(f"B 점수: {score_b}")

        if result == "UNDECIDED":
            print("판정: 판정 불가")
        else:
            print(f"판정: {result}")

    if mode == "2":
        print("data.json 분석 모드를 선택했습니다.")


if __name__ == "__main__":
    main()