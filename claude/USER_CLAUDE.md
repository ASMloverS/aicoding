# User-Level CLAUDE.md

## Precision Editing Protocol

### Reading: Locate-Window-Verify
- Never read a file from line 1 unless a full-file survey is required.
- Grep for the target symbol first, then Read with offset/limit (max 300 lines per call).
- Always include ±20 lines around the target to confirm context before editing.

### Writing: The 100-Line Rule
- Never modify more than **100 lines** in a single Edit or Write call.
- For larger changes, split into logical sub-steps following the **Edit-Verify** cycle:
  1. Apply a sub-change (≤100 lines).
  2. Run a quick syntax/build check (e.g., `cmake --build build`, `g++ -fsyntax-only`).
  3. Repeat for the next sub-change.
- For global renames or refactors affecting 1000+ lines, prefer generating a `.patch` file or using `sed`, not Edit.

### Forbidden
- No mega-edits: do not refactor multiple functions in a single Edit call.
- No blind overwrites: always Grep/Read to confirm current state before writing.

## Git Commit Convention
- Never append `Co-Authored-By: Claude ...` to any git commit message.
