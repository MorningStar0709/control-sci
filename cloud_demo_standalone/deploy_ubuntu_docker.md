# Ubuntu Docker Deployment

This is the intended cloud deployment path for the standalone pure-cloud demo. The package runs two containers:

- `controlmind-cloud-web`: Next.js Starboard-style workbench.
- `controlmind-cloud-api`: FastAPI cloud proxy for MinerU official API, DeepSeek question generation, and DeepSeek grading.

The local full demo folders `starboard/` and `controlsci/` are not required on the cloud server.

## 1. Server

Recommended minimum:

- Ubuntu 22.04 or 24.04
- Docker Engine with Compose plugin
- 1 vCPU / 1 GB RAM for the lightweight demo
- Public network access to MinerU official API and DeepSeek API

## 2. Upload The Folder

Copy only this folder:

```bash
scp -r cloud_demo_standalone user@server:/opt/controlmind-cloud-demo
```

## 3. Configure Environment

```bash
cd /opt/controlmind-cloud-demo
cp .env.example .env
nano .env
```

Required for live calls:

```bash
MINERU_API_TOKEN=<mineru-api-token>
DEEPSEEK_API_KEY=<deepseek-api-key>
```

Recommended:

```bash
CLOUD_DEMO_PUBLIC_PORT=18080
DEMO_DAILY_LIMIT=100
DEMO_UPLOAD_MAX_MB=20
DEMO_ACCESS_CODE=<share-with-reviewers-if-needed>
```

Do not commit `.env` or bake keys into images.

## 4. Start

```bash
docker compose up -d --build
```

Check containers:

```bash
docker compose ps
curl http://127.0.0.1:18080/api/demo/health
curl http://127.0.0.1:18080/api/demo/runtime/options
curl http://127.0.0.1:18080/api/demo/tracks
```

Open the workbench:

```text
http://SERVER_IP:18080/demo
```

## 5. Logs

```bash
docker compose logs -f --tail=100 controlmind-cloud-web
docker compose logs -f --tail=100 controlmind-cloud-api
```

## 6. Update

```bash
cd /opt/controlmind-cloud-demo
docker compose down
docker compose up -d --build
```

The named volume `cloud-demo-data` keeps quota and uploaded public-demo files.

## 7. Nginx Optional Reverse Proxy

Use this if exposing through port 80/443:

```nginx
server {
    listen 80;
    server_name demo.example.com;

    client_max_body_size 20m;

    location / {
        proxy_pass http://127.0.0.1:18080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Add Basic Auth at Nginx if the demo is not meant to be fully public.

## 8. Acceptance

Run from the Ubuntu host:

```bash
curl http://127.0.0.1:18080/api/demo/health
curl http://127.0.0.1:18080/api/demo/runtime/options
curl http://127.0.0.1:18080/api/demo/tracks
```

Expected runtime policy:

- `mode`: `pure_cloud_only`
- `profiles`: only `pure_cloud_demo`
- `parser_backends`: only `mineru_official`
- `generation_backends`: only `deepseek`
- `local_models`: empty array
- `local_indexes`: empty array
- frontend exposes no API keys
- demo entrypoint uses the Next workbench, not a static HTML mock
- Track1 backend has parse, question generation, and grading endpoints

