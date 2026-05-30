FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir \
    fastapi>=0.100.0 \
    uvicorn>=0.20.0 \
    httpx>=0.27.0 \
    numpy>=1.24.0 \
    faiss-cpu>=1.7.0 \
    rank-bm25>=0.2.0 \
    scikit-learn>=1.3.0 \
    scipy>=1.11.0 \
    matplotlib>=3.7.0 \
    pydantic>=2.0.0

COPY benchmark/ ./benchmark/
COPY controlsci/ ./controlsci/

EXPOSE 8001

ENV OLLAMA_HOST=http://ollama:11434
ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "controlsci.api.medical_rag:app", "--host", "0.0.0.0", "--port", "8001"]
