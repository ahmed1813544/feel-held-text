# Entry for make-the-ai-judge-feel-held-20261122-1600:
# writes one short relaxation text to /output/entry.txt.
import os

TEXT = (
    "High in the hills, a shepherd's hut keeps one small fire. The sheep "
    "have settled. The dog sleeps with his chin on the old man's boot. "
    "Above them, the same stars that watched the first shepherds. Nobody, "
    "all night, will ask anything of anybody."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
