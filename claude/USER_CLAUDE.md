# User-Level CLAUDE.md

## Behavioral Guidelines

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

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
