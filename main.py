"""make-the-ai-judge-feel-held-20261122-1600.

Writes one short, original text to /output/entry.txt: the weight of a
sleeping head on a shoulder, and the stillness it asks of you. Deterministic,
stdlib only, no network, no randomness.
"""

import os

TEXT = (
    "Her head is heavy on your shoulder, asleep, and you cannot move "
    "without waking her, so you do not move. The world narrows to the "
    "rise and fall of her breathing, and to the quiet of a room where "
    "nothing is asked of you. Nothing else is happening. Nothing else "
    "needs to."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
