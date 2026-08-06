from pathlib import Path

ROOT = Path("app")

SKIP_DIRS = {
    ".git",
    "venv",
    ".venv",
    "__pycache__",
    "node_modules",
}

TEXT_EXTENSIONS = {
    ".py",
    ".html",
    ".css",
    ".js",
    ".json",
    ".txt",
    ".md",
    ".yml",
    ".yaml",
}


def clean_conflicts(content):
    lines = content.splitlines(keepends=True)

    output = []
    head_block = []

    state = "normal"

    conflicts = 0

    for line in lines:

        if line.startswith("<<<<<<<"):
            state = "head"
            head_block = []
            conflicts += 1
            continue

        if state == "head" and line.startswith("======="):
            state = "incoming"
            continue

        if state == "incoming" and line.startswith(">>>>>>>"):
            output.extend(head_block)
            head_block = []
            state = "normal"
            continue

        if state == "normal":
            output.append(line)

        elif state == "head":
            head_block.append(line)

        elif state == "incoming":
            # Incoming version intentionally discarded.
            pass

    # Do not silently destroy malformed conflict blocks.
    if state != "normal":
        raise ValueError(
            "Incomplete Git conflict block detected."
        )

    return "".join(output), conflicts


def main():

    files_changed = 0
    conflicts_removed = 0

    for path in ROOT.rglob("*"):

        if not path.is_file():
            continue

        if any(part in SKIP_DIRS for part in path.parts):
            continue

        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue

        try:
            content = path.read_text(encoding="utf-8")

        except UnicodeDecodeError:
            continue

        if "<<<<<<<" not in content:
            continue

        try:
            cleaned, count = clean_conflicts(content)

        except ValueError as error:
            print(f"SKIPPED: {path} - {error}")
            continue

        path.write_text(
            cleaned,
            encoding="utf-8",
        )

        files_changed += 1
        conflicts_removed += count

        print(
            f"CLEANED: {path} "
            f"({count} conflict block(s))"
        )

    print()
    print("-------------------------------")
    print("Conflict cleanup completed")
    print("-------------------------------")
    print(f"Files changed: {files_changed}")
    print(f"Conflicts removed: {conflicts_removed}")


if __name__ == "__main__":
    main()