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

COPY deps ./deps

RUN python -m venv /opt/venvs/flask \
    && /opt/venvs/flask/bin/pip install -r deps/flask.in

COPY . ./

RUN /opt/venvs/flask/bin/pip install -e .[flask]
