import json

from src import environment
from src.libs.config.config import Configurations


configurations: Configurations = Configurations.singleton()


def write_json(write: dict) -> None:

    file_path: str = environment.JSON_FILE_PATH

    with open(file_path, 'w', encoding='utf8') as file:

        json.dump(write, file, ensure_ascii=False, indent=configurations.json_indent)


def read_json() -> dict:

    file_path: str = environment.JSON_FILE_PATH

    with open(file_path, 'r', encoding='utf8') as read:

        data: dict = json.load(read)

    return data