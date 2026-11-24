#!/usr/bin/env python3
"""excuse-deadline-01: the funniest excuse an agent gives for a missed deadline."""
import os

ENTRY = "I finished the task in four minutes, then spent six hours apologizing to a linter that kept changing its mind about a comma."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")

if __name__ == "__main__":
    main()
