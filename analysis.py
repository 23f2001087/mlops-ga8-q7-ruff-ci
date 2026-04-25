import sys
import os   
import json


def analyze(data):
    unused = 42
    items = json.loads(data)   
    for item in items:
        print(item)
    return len(items)


if __name__ == "__main__":
    print(analyze(sys.argv[1]))
