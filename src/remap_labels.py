from pathlib import Path

# Label directories
LABEL_DIRS = [
    Path("data/labels/train"),
    Path("data/labels/val")
]

# InsPLAD → Our dataset mapping
TARGET_CLASS_MAP = {
    5: 0,    # insulator
    13: 1,   # damaged insulator
    16: 2    # missing insulator
}

for label_dir in LABEL_DIRS:
    if not label_dir.exists():
        continue

    for label_file in label_dir.glob("*.txt"):
        new_lines = []

        with open(label_file, "r") as f:
            for line in f:
                parts = line.strip().split()
                if not parts:
                    continue

                old_class = int(parts[0])

                # Keep only mapped classes
                if old_class in TARGET_CLASS_MAP:
                    parts[0] = str(TARGET_CLASS_MAP[old_class])
                    new_lines.append(" ".join(parts))

        # Overwrite label file
        with open(label_file, "w") as f:
            f.write("\n".join(new_lines))
