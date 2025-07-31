# typed inputs for validation, define clear tool signatures like Dict[str, Union[str, int]] for inputs

from typing import List, Dict

def summarize_table(rows: List[Dict[str, str]]) -> str:
    return f"found {len(rows)} rows"

inp: List[Dict[str, str]] = [
    {
        "id": 111,
        "name": "mir"
    }
]
print(summarize_table(inp))