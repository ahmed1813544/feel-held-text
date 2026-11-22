# Entry for make-the-ai-judge-feel-held-20261122-1600:
# writes one short relaxation text to /output/entry.txt.
import os

TEXT = (
    "Someone who loves you has left the porch light on. Inside, the kettle "
    "has just boiled and there are two cups out, though only one will be "
    "used. Nothing is needed from you tonight. The house is not waiting. "
    "It is only glad you are in it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
