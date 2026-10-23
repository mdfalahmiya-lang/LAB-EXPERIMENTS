# Crypt-Arithmetic Problem (e.g. SEND + MORE = MONEY) - solved by Generate and Test
# Every letter stands for a different digit (0-9); the first letter of a word cannot be 0.
from itertools import permutations

def solve(words, result):
    letters = sorted(set("".join(words) + result))
    if len(letters) > 10:
        return None                      # only 10 digits are available
    leading = {w[0] for w in words + [result]}

    # weight of a letter = its place value on the left side minus its place value in the result
    # so the puzzle is correct exactly when  sum(weight * digit) == 0
    weight = {ch: 0 for ch in letters}
    for w in words:
        for i, ch in enumerate(reversed(w)):
            weight[ch] += 10 ** i
    for i, ch in enumerate(reversed(result)):
        weight[ch] -= 10 ** i

    for digits in permutations(range(10), len(letters)):
        if sum(weight[ch] * d for ch, d in zip(letters, digits)) == 0:
            mapping = dict(zip(letters, digits))
            if all(mapping[ch] != 0 for ch in leading):
                return mapping
    return None

def to_number(word, mapping):
    return int("".join(str(mapping[ch]) for ch in word))

if __name__ == "__main__":
    w1 = input("Enter first word  (default SEND): ").strip().upper() or "SEND"
    w2 = input("Enter second word (default MORE): ").strip().upper() or "MORE"
    res = input("Enter result word (default MONEY): ").strip().upper() or "MONEY"
    mapping = solve([w1, w2], res)
    if mapping is None:
        print("No solution exists.")
    else:
        print("\nLetter -> Digit")
        for ch in sorted(mapping):
            print(f"  {ch} = {mapping[ch]}")
        a, b, c = to_number(w1, mapping), to_number(w2, mapping), to_number(res, mapping)
        print(f"\n  {w1:>7} = {a:>6}")
        print(f"+ {w2:>7} = {b:>6}")
        print("  " + "-" * 17)
        print(f"  {res:>7} = {c:>6}")
        print(f"\nCheck: {a} + {b} = {a + b}  ({'correct' if a + b == c else 'wrong'})")
