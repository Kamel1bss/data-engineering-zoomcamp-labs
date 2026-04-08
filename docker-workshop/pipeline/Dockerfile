FROM python:3.13.11-slim

# Install uv and its dependencies
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code 

ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./

# Install python dependencies
RUN pip install pandas pyarrow 

RUN uv sync --locked

COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]