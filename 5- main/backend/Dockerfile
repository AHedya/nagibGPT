FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt pyproject.toml /app/
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels -r requirements.txt
COPY src src
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels .

FROM python:3.10-slim AS runner
COPY --from=builder /app/wheels /wheels 
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels 
COPY --from=builder /app/src /app/src  

EXPOSE 8000
WORKDIR /app/src

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
