import sys

src: str = sys.stdin.read()

print("{", end="")

for c in src:
    print(f"{ord(c)}, ", end="")

print("}", end="")