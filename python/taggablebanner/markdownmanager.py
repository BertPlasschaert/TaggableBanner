import datetime
from pathlib import Path

START_MARKER = "<!--begin usernames-->\n"
END_MARKER = "<!--end usernames-->\n"

MD_FILE = Path("README.md")


def _get_md_lines(file_path: Path) -> list[str]:
    with open(file_path) as f:
        return f.readlines()


def _get_name_lines(lines: list[str]) -> list[str]:
    start_index: int = lines.index(START_MARKER) + 1
    end_index: int = lines.index(END_MARKER)

    return lines[start_index:end_index]


def _extract_names(lines: list[str]) -> list[str]:
    names: list[str] = list()
    for line in lines:
        try:
            names.append(line.split("[")[1].split("]")[0])
        except IndexError as e:
            raise ValueError(f"name values in README.md might be mallformed: {e}")

    return names


def get_names() -> list[str]:
    lines = _get_md_lines(MD_FILE)
    name_lines = _get_name_lines(lines)
    return _extract_names(name_lines)


def add_name(name: str) -> None:
    md_lines = _get_md_lines(MD_FILE)
    end_index = md_lines.index(END_MARKER)
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    md_lines.insert(end_index, f"###### [{name}] on {date}\n")

    with open(MD_FILE, "w") as f:
        f.writelines(md_lines)
