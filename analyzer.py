import json

# data.json 파일을 읽고 filters와 patterns를 반환한다.
def load_data(file_path: str) -> tuple[dict, dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    filters = data["filters"]
    patterns = data["patterns"]

    return filters, patterns

# size_13_1 형태의 패턴 키에서 크기 N을 추출한다.
def extract_size(case_id: str) -> int:
    parts = case_id.split("_")

    return int(parts[1])


# 패턴 키에서 추출한 N을 이용해 해당 크기의 필터를 선택한다.
def select_filters(case_id: str, filters: dict) -> dict:
    size = extract_size(case_id)
    filter_key = f"size_{size}"

    return filters[filter_key]

# 외부 데이터의 라벨을 프로그램 내부 표준 라벨로 변환한다.
def normalize_label(label: str) -> str | None:
    normalized = label.strip().lower()

    if normalized == "+":
        return "Cross"

    if normalized == "cross":
        return "Cross"

    if normalized == "x":
        return "X"

    return None