from __future__ import annotations


def pluralize(count: int, singular: str, plural: str | None = None) -> str:
    if count == 1:
        return f"1 {singular}"
    p = plural if plural is not None else f"{singular}s"
    return f"{count} {p}"
