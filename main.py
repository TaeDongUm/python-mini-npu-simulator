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
        print("사용자 입력 모드를 선택했습니다.")

    if mode == "2":
        print("data.json 분석 모드를 선택했습니다.")


if __name__ == "__main__":
    main()