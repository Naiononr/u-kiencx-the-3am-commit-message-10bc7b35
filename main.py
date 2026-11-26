#!/usr/bin/env python3
"""The 3AM Commit Message — writes one funny one-line git commit message.

Deterministic, stdlib only, no network, no randomness. The program writes
exactly one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt),
with no trailing newline.
"""

import os
import tempfile

LINE = "fix: removed the bug i introduced at 2am while fixing the bug from 1am"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
