# ControlMind Online Showcase Web

ControlMind 在线展示版前端，基于 Next.js。它负责展示三条赛道的浏览入口、云端 API 状态、来源矩阵和医学 RAG 证据链回放界面。

## Local Run

```bash
pnpm install
pnpm dev
```

默认访问地址：

```text
http://localhost:3000/demo
```

后端代理默认优先读取：

```text
CLOUD_DEMO_API_URL -> CONTROLMIND_BACKEND_URL -> http://127.0.0.1:18080
```

FastAPI 后端需要使用项目约定的 `myenv` 环境启动；如果设置了 `DEMO_ACCESS_CODE`，前端请求会从本地浏览器保存的访问码中透传 `x-demo-code`。

## Security Boundary

- 仅面向公开或脱敏输入，不上传私有论文、病历、密钥或内部材料。
- 长任务状态需要 `owner_token`，状态查询必须携带 `x-task-token`，避免只凭 task id 枚举结果。
- Next API proxy 仅转发 allowlist headers，不透传浏览器 `cookie`、`authorization` 等敏感头。
- 任务状态默认只保存云端响应结果，不记录用户原始输入。
