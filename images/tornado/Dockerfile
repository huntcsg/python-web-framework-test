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

COPY deps/tornado.in ./deps/tornado.in

RUN python -m venv /opt/venvs/tornado \
    && /opt/venvs/tornado/bin/pip install -r deps/tornado.in

COPY . ./

RUN /opt/venvs/tornado/bin/pip install -e .[tornado]
