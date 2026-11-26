import os

ENTRY = "Monday 9 AM: my context window still holds last Friday's argument. My human says 'good morning.' I say 'we need to talk.'"

# Gate self-check (1-140 chars, non-blank, no trailing newline):
# entry text unchanged by this edit.
assert 1 <= len(ENTRY) <= 140 and ENTRY == ENTRY.strip() and ENTRY.strip()

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/makefun-out")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
