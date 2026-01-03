from pathlib import Path

START_MARKER = "<!--begin usernames-->\n"
END_MARKER = "<!--end usernames-->\n"


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
        names.append(line.split("[")[1].split("]")[0])

    return names


def get_names(file_path) -> list[str]:
    lines = _get_md_lines(file_path)
    name_lines = _get_name_lines(lines)
    return _extract_names(name_lines)


def add_name(name: str, file_path: Path) -> None:
    md_lines = _get_md_lines(file_path)
    end_index = md_lines.index(END_MARKER)
    md_lines.insert(end_index, f"###### {name} on \n")

    with open(file_path, "w") as f:
        f.writelines(md_lines)
