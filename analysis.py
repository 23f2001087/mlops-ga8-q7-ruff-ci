import json
import sys


def analyze(data):
    items = json.loads(data)
    for item in items:
        print(item)
    return len(items)


if __name__ == "__main__":
    print(analyze(sys.argv[1]))
