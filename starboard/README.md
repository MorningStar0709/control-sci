# ControlMind Starboard

ControlMind 科学复现工作台前端，基于 Next.js。它负责展示三条赛道的本地复现入口、依赖状态、来源矩阵和医学 RAG 问答界面。

## Local Run

```powershell
pnpm install --frozen-lockfile
pnpm dev
```

默认访问地址：

```text
http://localhost:3000
```

后端代理默认指向：

```text
http://127.0.0.1:17001
```

如需连接其他后端地址，可设置：

```powershell
$env:CONTROLMIND_BACKEND_URL='http://127.0.0.1:17001'
pnpm dev
```

构建检查：

```powershell
pnpm lint
pnpm build
```

FastAPI 后端需要使用项目约定的 `myenv` 环境启动。

公开部署限制：Next.js API 代理必须能访问私有 FastAPI 后端；医学原文、chunk、索引和检索上下文默认不随前端部署。若只做公开展示，请使用 `demo_replay` / evidence-only 模式。

公开部署安全边界：

- 长任务状态需要 `owner_token` 才能读取，避免仅凭 task id 查看结果。
- 任务状态默认不回显原始 input；仅在 `STARBOARD_DEBUG_TASK_INPUT=true` 时返回脱敏后的 input 方便调试。
- Next.js API 代理只转发最小 allowlist headers，不转发浏览器 cookie、authorization 或其他凭证。
- 当前任务存储是单实例内存 Map，仅适合本地或单实例公开 Demo；长期公网部署建议替换为 SQLite / Redis 并增加访问码或速率限制。
