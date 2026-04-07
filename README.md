# Agent Platform (Python, Minimal)

一个保持简洁、可运行、可提交的 Python Agent 开发骨架。

## 标准流程

1. 启动容器

```bash
./scripts/up.sh
```

2. 在 VS Code 中执行 Dev Containers: Reopen in Container

3. 进入 Agent 项目并初始化环境

```bash
cd agents/claude-adk
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .[dev]
```

4. 本地运行与测试

```bash
python -m src.main
python -m pytest
```

5. 提交与推送

```bash
cd /workspace
git add .
git commit -m "feat: your change"
git push
```

## 清理规则

- 删除缓存文件：`.pytest_cache`、`__pycache__`、`.DS_Store`、`*.pyc`
- `.venv` 仅作为本地运行环境保留，不提交到仓库
- 不引入重复脚本和过度封装，优先保持最小可维护改动

## 项目结构

- `.devcontainer/`: 容器开发配置
- `docker/compose.yml`: 运行编排
- `agents/claude-adk/`: Python Agent 代码
- `scripts/`: 启停脚本
