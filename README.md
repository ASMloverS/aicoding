# AI Coding Configuration Standards

> 统一的 AI 编程助手代码风格配置标准 / Unified coding style standards for AI programming assistants

本项目旨在为不同的 AI 编程助手和代理建立统一的 Python 代码风格指南和文档标准，确保在各种 AI 驱动的开发工具之间保持一致的代码风格。

This project establishes unified Python coding style guidelines and documentation standards for various AI programming assistants and agents, ensuring consistent code style across different AI-powered development tools.

## Project Structure

```
aicoding/
├── py_guide.py          # Python 代码风格参考模板 / Python style guide reference
├── claude/              # Claude Code 配置指南 / Claude Code guidelines
├── codex/               # Codex AI 代理指南 / Codex AI agent guidelines
├── kimi/                # Kimi AI 代理指南 (中文) / Kimi AI agent guidelines (Chinese)
└── opencode/            # OpenCode 代理指南 / OpenCode agent guidelines
```

## Components

| Directory | Description | Language |
|-----------|-------------|----------|
| `claude/` | Claude Code specific guidance | English |
| `codex/` | Codex AI agent guidelines | English |
| `kimi/` | Kimi AI agent guidelines | Chinese |
| `opencode/` | OpenCode agent guidelines | English |

## Python Style Guide

The `py_guide.py` file serves as the canonical reference for Python coding style, covering:

- File headers (shebang, encoding declaration)
- Module docstrings with usage examples
- Import ordering (standard library → third-party → local)
- Type hints using modern Python 3.10+ syntax (`|` unions)
- Function docstrings with tree-style formatting
- Class docstrings with Attributes section
- Constants naming conventions (UPPER_SNAKE_CASE)

## Supported AI Assistants

- [Claude Code](https://claude.com/claude-code)
- Codex AI
- [Kimi AI](https://kimi.moonshot.cn/)
- OpenCode

## License

MIT
