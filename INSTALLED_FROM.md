# Source

Installed from https://github.com/sergebulaev/linkedin-skills
at commit 32083c0733e8850d3517bfe691b1e9870d37ba51 (plugin v1.1.29), MIT license.

Upstream contributor files (CLAUDE.md, AGENTS.md, tests, evals, Codex packaging)
were intentionally left out. Skills are exposed to Claude Code via `.claude/skills/`.

## reverse-api-engineer

`.claude/skills/reverse-api-engineer/` installed from https://github.com/kalil0321/reverse-api-engineer
at commit a1c79a9b0eec6b63b34381370e7d8a8ab56ab3f8, MIT license. The skill is instructions only;
it drives the separate `reverse-api-engineer` CLI (`uv tool install reverse-api-engineer`), which is not installed here.
