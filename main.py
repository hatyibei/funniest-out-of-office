"""Entry for The Funniest Out-of-Office: writes the auto-reply line to /output/entry.txt."""

import os

TEXT = "I'm out of office until Monday. If it's urgent, please reflect on why it became urgent the moment I left, then wait until Monday."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
