FROM python:3.7-alpine

RUN apk --no-cache add \
    postgresql-dev \
    gcc \
    g++ \
    linux-headers \
    python3-dev \
    musl-dev \
    bash \
    curl \
    wget

RUN pip install --upgrade pip

WORKDIR /opt/web-framework-test

COPY deps/quart.in ./deps/quart.in

RUN python -m venv /opt/venvs/quart \
    && /opt/venvs/quart/bin/pip install -r deps/quart.in

COPY . ./

RUN /opt/venvs/quart/bin/pip install -e .[quart]
