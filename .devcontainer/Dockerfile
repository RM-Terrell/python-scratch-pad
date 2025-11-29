FROM debian:stable-slim

RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN useradd -ms /bin/bash vscode

USER vscode
WORKDIR /workspaces/python-scratch-pad

ENV UV_LINK_MODE=copy
ENV UV_PYTHON_DOWNLOADS=auto

CMD ["bash"]
