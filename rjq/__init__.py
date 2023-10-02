import json
import sys
from subprocess import run as run_cmd
from typing import Any


def run():
    obj = parse_json(sys.stdin.read())
    run_cmd(["jq", *sys.argv[1:]], input=json.dumps(obj).encode())


def parse_json(data: Any, return_raw=False) -> Any:
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            if return_raw:
                return data
            raise

    if isinstance(data, list):
        return [parse_json(obj, True) for obj in data]
    if isinstance(data, dict):
        return {k: parse_json(v, True) for k, v in data.items()}

    return data
