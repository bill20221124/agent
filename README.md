# Agent Platform (Python, Minimal)

最小可运行的 VS Code + Docker + Python Agent 开发骨架。

## 使用

1. 打开项目目录。
2. 启动容器：

```bash
./scripts/up.sh
```

3. VS Code 执行 `Dev Containers: Reopen in Container`。
4. 容器内运行：

```bash
python -m src.main
```

## 停止

```bash
./scripts/down.sh
```

## 结构

- .devcontainer/: 容器开发配置
- docker/compose.yml: 运行编排
- agents/claude-adk/: Python 代码
- scripts/: 启停脚本
