# ControlMind Pure Cloud Demo

This folder is an isolated cloud demo package. It keeps the local full demo untouched and packages a lightweight Starboard-style Next.js workbench with a standalone FastAPI cloud API.

## What Is Included

- `web/`: Next.js workbench copied from the Starboard shell and adapted to pure cloud mode.
- `app.py`: standalone API proxy for MinerU official API, DeepSeek question generation, and DeepSeek grading.
- `docker-compose.yml`: Ubuntu cloud deployment with separate web and API containers.
- `verify.ps1`: API smoke verification.
- `verify_workbench.ps1`: local workbench verification.

## Cloud Boundary

- Public or desensitized inputs only.
- MinerU and DeepSeek keys are read only by the server.
- No local model switch, no private index, no local GPU/offline execution path.
- Built-in sample PDF is hidden behind the "内置样例" button instead of being shown in the URL box.
- Track1 backend exposes parse, quiz generation, and grading APIs.

## Local Development

Run the API and the Next workbench:

```powershell
.\cloud_demo_standalone\start_workbench.ps1 -Force
```

Open:

```text
http://127.0.0.1:18081/demo
```

API-only smoke run:

```powershell
.\cloud_demo_standalone\start.ps1 -Force
.\cloud_demo_standalone\verify.ps1
```

Workbench verification:

```powershell
.\cloud_demo_standalone\verify_workbench.ps1
```

## Environment

Set these for live cloud calls:

```powershell
$env:MINERU_API_TOKEN="<mineru-api-token>"
$env:DEEPSEEK_API_KEY="<deepseek-api-key>"
```

Optional:

```powershell
$env:CLOUD_DEMO_PORT="18080"
$env:DEMO_DAILY_LIMIT="100"
$env:DEMO_UPLOAD_MAX_MB="20"
$env:DEMO_ACCESS_CODE="optional-code"
```

If `DEMO_ACCESS_CODE` is set, live API calls must include that code.

## Ubuntu Docker

On the cloud server:

```bash
cd /opt/controlmind-cloud-demo
cp .env.example .env
nano .env
docker compose up -d --build
curl http://127.0.0.1:18080/api/demo/health
```

The public entrypoint is the Next workbench at:

```text
http://SERVER_IP:18080/demo
```

See `deploy_ubuntu_docker.md` for the full Ubuntu procedure.

