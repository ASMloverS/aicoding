# AI Coding Configuration Standards

> 统一的 AI 编程助手代码风格配置标准 / Unified coding style standards for AI programming assistants

本项目为不同的 AI 编程助手和代理建立统一的代码风格指南（基于 PEP 8）、Git 提交规范（gitmoji）以及模型配置模板，确保在各种 AI 驱动的开发工具之间保持一致的代码风格和工作流。

This project establishes unified coding style guidelines (based on PEP 8), Git commit conventions (gitmoji), and model configuration templates for various AI programming assistants and agents.

## Project Structure

```
aicoding/
├── .claude/                     # Claude Code 本地设置 / Claude Code local settings
│   └── settings.local.json
├── claude/                      # Claude Code 配置 / Claude Code config
│   ├── CLAUDE.md                #   代码风格与提交规范 / Style & commit guidelines
│   ├── USER_CLAUDE.md           #   用户级自定义配置 / User-level custom config
│   ├── settings.glm.json        #   GLM 模型配置 / GLM model config
│   ├── settings.kimi.json       #   Kimi 模型配置 / Kimi model config
│   └── settings.minimax.json    #   MiniMax 模型配置 / MiniMax model config
├── codex/                       # Codex AI 代理指南 / Codex AI agent guidelines
│   └── AGENTS.md
├── kimi/                        # Kimi AI 代理指南 / Kimi AI agent guidelines
│   └── AGENTS.md
├── opencode/                    # OpenCode 代理指南与配置 / OpenCode agent guidelines & config
│   ├── AGENTS.md
│   ├── opencode.glm.json        #   GLM 模型配置 / GLM model config
│   └── opencode.minimax.json    #   MiniMax 模型配置 / MiniMax model config
└── skills/                      # Claude Code 技能 / Claude Code skills
    ├── pyinit/                  #   Python 项目初始化 (EN) / Python project init (EN)
    ├── pyinit-cn/               #   Python 项目初始化 (CN) / Python project init (CN)
    └── pyinit.skill             #   技能定义文件 / Skill definition file
```

## Components

| Directory | Description | Key Content |
|-----------|-------------|-------------|
| `.claude/` | Claude Code local settings | Local project settings |
| `claude/` | Claude Code configuration | Style guide, commit conventions, model configs (GLM/Kimi/MiniMax) |
| `codex/` | Codex AI agent guidelines | PEP 8 code rules, commit message rules |
| `kimi/` | Kimi AI agent guidelines | Coding standards, gitmoji commit conventions |
| `opencode/` | OpenCode agent guidelines | Build commands, style guide, model configs |
| `skills/` | Claude Code reusable skills | Python project scaffolding (EN & CN) |

## Coding Style

All AI assistants share a unified Python coding style based on **PEP 8 / PEP 257**:

- UTF-8 encoding, Unix line endings (LF), 4-space indentation
- Max line length: 79 (code) / 72 (docstrings & comments)
- Import order: stdlib → third-party → local (separated by blank lines)
- Naming: `snake_case` (functions/variables), `PascalCase` (classes), `UPPER_SNAKE_CASE` (constants)
- Type hints required (Python 3.10+ `|` union syntax)
- Google-style docstrings with `Args:`, `Returns:`, `Raises:` sections

## Git Commit Convention

All assistants follow the **gitmoji** commit format:

```
<gitmoji> <type>(<scope>): <description>
```

Examples:
- `:sparkles: feat(auth): add OAuth2 login support`
- `:bug: fix(parser): handle empty input gracefully`
- `:memo: docs(README): update installation instructions`

## Supported AI Assistants

- [Claude Code](https://claude.com/claude-code)
- Codex AI
- [Kimi AI](https://kimi.moonshot.cn/)
- [OpenCode](https://opencode.ai/)

## License

MIT
