import json

# data.json 파일을 읽고 filters와 patterns를 반환한다.
def load_data(file_path: str) -> tuple[dict, dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    filters = data["filters"]
    patterns = data["patterns"]

    return filters, patterns