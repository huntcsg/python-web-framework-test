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

COPY deps/pyramid.in ./deps/pyramid.in

RUN python -m venv /opt/venvs/pyramid \
    && /opt/venvs/pyramid/bin/pip install -r deps/pyramid.in

COPY . ./

RUN /opt/venvs/pyramid/bin/pip install -e .[pyramid]
