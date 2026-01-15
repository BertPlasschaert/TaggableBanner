# stdlib modules
import datetime
from pathlib import Path

# tool modules
from taggablebanner.const import MD_FILE
from taggablebanner.const import MD_START_MARKER
from taggablebanner.const import MD_END_MARKER


def _validate_md_file(file_path: Path):
    """Check if markdown file has correct contents."""

    lines = _get_md_lines(file_path)
    if MD_END_MARKER not in lines or MD_END_MARKER not in lines:
        raise ValueError(
            f"Markdown file: {file_path} has no valid begin or end markers"
        )


def _generate_minimal_md_file(file_path: Path):
    """Generate an README.md file with the required markers"""
    file_path.write_text(f"{MD_START_MARKER}{MD_END_MARKER}")


def _get_md_lines(file_path: Path) -> list[str]:
    """Read all lines of the provided file path."""
    with open(file_path) as f:
        return f.readlines()


def _get_name_lines(lines: list[str]) -> list[str]:
    """Filter out all the name lines from the provided list of lines."""
    start_index: int = lines.index(MD_START_MARKER) + 1
    end_index: int = lines.index(MD_END_MARKER)

    return lines[start_index:end_index]


def _extract_names(lines: list[str]) -> list[str]:
    """Filter out all the usernames from the provided list of name lines."""
    names: list[str] = list()
    for line in lines:
        try:
            names.append(line.split("[")[1].split("]")[0])
        except IndexError as e:
            raise ValueError(f"name values in README.md might be mallformed: {e}")

    return names


def get_names() -> list[str]:
    """Get username from markdown file."""

    if not MD_FILE.exists():
        return []

    _validate_md_file(MD_FILE)
    lines = _get_md_lines(MD_FILE)
    name_lines = _get_name_lines(lines)
    return _extract_names(name_lines)


def add_name(name: str) -> None:
    """Add provided username to markdown file."""

    if not MD_FILE.exists():
        _generate_minimal_md_file(MD_FILE)

    _validate_md_file(MD_FILE)
    md_lines = _get_md_lines(MD_FILE)
    end_index = md_lines.index(MD_END_MARKER)
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    md_lines.insert(
        end_index, f"###### [{name}](https://github.com/{name}) on {date}\n"
    )

    with open(MD_FILE, "w") as f:
        f.writelines(md_lines)
