from __future__ import annotations
def parse_seat_codes(codes_str: str):
    out = []
    for raw in (codes_str or '').split(','):
        s = raw.strip().upper()
        if not s: continue
        row = ''.join(ch for ch in s if ch.isalpha())
        col = ''.join(ch for ch in s if ch.isdigit())
        if not row or not col:
            raise ValueError(f"Invalid seat code: {raw!r} (use A1, B10, ...)")
        out.append((row, int(col)))
    return out

def make_row_labels(n: int):
    labels, i = [], 0
    while len(labels) < n:
        labels.append(_num_to_letters(i)); i += 1
    return labels

def _num_to_letters(n: int) -> str:
    s = ''
    while True:
        n, r = divmod(n, 26)
        s = chr(ord('A') + r) + s
        if n == 0: break
        n -= 1
    return s
